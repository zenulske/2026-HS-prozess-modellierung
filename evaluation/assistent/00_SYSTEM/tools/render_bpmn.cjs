// Shared adapter around unchanged bpmn-js and sharp; no BPMN drawing logic.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { parseArgs } = require('node:util');
const digest = b => crypto.createHash('sha256').update(b).digest('hex');
const fail = (code, message) => { throw Object.assign(new Error(message), { code }); };

async function main() {
  const { values: a } = parseArgs({ options: Object.fromEntries([
    'input', 'output', 'packages', 'channel', 'browser', 'diagram-id',
    'environment', 'approved-environment'].map(k => [k, { type: 'string' }])) });
  if (!a.environment || a.environment !== a['approved-environment'])
    fail('PRIVACY_REQUIRED', 'Human approval for this environment is required.');
  for (const k of ['input', 'output', 'packages'])
    if (!a[k] || !path.isAbsolute(a[k])) fail('ARGUMENT_REQUIRED', `Absolute --${k} required.`);
  if (a.channel && a.browser) fail('ARGUMENT_INVALID', 'Choose channel or browser, not both.');
  const output = path.resolve(a.output);
  if (fs.existsSync(output)) fail('OUTPUT_EXISTS', 'Choose a new preview directory; no overwrite.');
  const parent = path.dirname(output);
  if (!fs.statSync(parent).isDirectory()) fail('OUTPUT_PARENT', 'Output parent must already exist.');
  const viewer = path.join(__dirname, 'renderer', 'bpmn-viewer.js');
  const lock = JSON.parse(fs.readFileSync(path.join(__dirname, 'renderer', 'LOCK.json')));
  const viewerBytes = fs.readFileSync(viewer);
  if (digest(viewerBytes) !== lock.sha256) fail('RENDERER_INTEGRITY', 'Viewer hash differs.');
  let chromium, sharp, playwrightVersion, sharpVersion;
  try {
    ({ chromium } = require(path.join(a.packages, 'playwright')));
    sharp = require(path.join(a.packages, 'sharp'));
    playwrightVersion = require(path.join(a.packages, 'playwright/package.json')).version;
    sharpVersion = require(path.join(a.packages, 'sharp/package.json')).version;
  } catch { fail('RENDERER_UNAVAILABLE', 'Existing compatible Playwright and sharp packages required; nothing installed.'); }
  let browser;
  try {
    browser = await chromium.launch({ headless: true,
      ...(a.channel ? { channel: a.channel } : {}),
      ...(a.browser ? { executablePath: a.browser } : {}) });
  } catch { fail('RENDERER_UNAVAILABLE', 'Existing Chromium browser unavailable; nothing downloaded.'); }
  try {
    const raw = fs.readFileSync(a.input);
    const xml = new TextDecoder('utf-8', { fatal: true }).decode(raw);
    if (/<!DOCTYPE|<!ENTITY/i.test(xml)) fail('XML_DECLARATION', 'DTD/entities unsupported.');
    const context = await browser.newContext({ offline: true, serviceWorkers: 'block' });
    await context.route('**/*', route => route.abort());
    const page = await context.newPage();
    await page.setViewportSize({ width: 1280, height: 900 });
    await page.setContent('<html><body style="margin:0"><div id="canvas" style="width:1280px;height:900px"></div></body></html>');
    await page.addScriptTag({ content: viewerBytes.toString('utf8') });
    const result = await page.evaluate(async ({ xml, diagramId }) => {
      const doc = new DOMParser().parseFromString(xml, 'application/xml');
      if (doc.querySelector('parsererror')) throw new Error('Invalid XML.');
      const ids = Array.from(doc.getElementsByTagNameNS('http://www.omg.org/spec/BPMN/20100524/DI', 'BPMNDiagram')).map(d => d.getAttribute('id'));
      if (!ids.length) throw new Error('No BPMNDiagram.');
      if (!diagramId && ids.length !== 1) throw new Error('Multiple diagrams: specify --diagram-id.');
      const selected = diagramId || ids[0];
      if (!selected || !ids.includes(selected)) throw new Error('Unknown diagram ID.');
      const viewer = new BpmnJS({ container: '#canvas' });
      const imported = await viewer.importXML(xml, selected);
      const { svg } = await viewer.saveSVG();
      return { svg, diagramId: selected, availableDiagrams: ids,
        warnings: imported.warnings.map(w => w.message) };
    }, { xml, diagramId: a['diagram-id'] });
    const png = await sharp(Buffer.from(result.svg), { density: 144 })
      .flatten({ background: '#fff' }).png().toBuffer();
    if (digest(fs.readFileSync(a.input)) !== digest(raw)) fail('SOURCE_CHANGED', 'Source changed during rendering.');
    const report = {
      source: path.resolve(a.input), sourceSha256: digest(raw),
      diagramId: result.diagramId, availableDiagrams: result.availableDiagrams,
      renderer: `bpmn-js ${lock.version}`, viewerSha256: digest(viewerBytes),
      playwrightVersion, sharpVersion, browserVersion: browser.version(),
      platform: process.platform, architecture: process.arch, warnings: result.warnings,
      svgSha256: digest(Buffer.from(result.svg)), pngSha256: digest(png),
      status: 'rendered; visual and native checks not performed',
    };
    fs.mkdirSync(output); // Deliberately exclusive, no recursive overwrite.
    fs.writeFileSync(path.join(output, 'preview.svg'), result.svg, { flag: 'wx' });
    fs.writeFileSync(path.join(output, 'preview.png'), png, { flag: 'wx' });
    fs.writeFileSync(path.join(output, 'provenance.json'), JSON.stringify(report, null, 2) + '\n', { flag: 'wx' });
    console.log(JSON.stringify({ ok: true, output, ...report }));
  } finally { await browser.close(); }
}
main().catch(e => {
  console.error(JSON.stringify({ ok: false, code: e.code || 'RENDER_FAILED', message: e.message,
    instruction: 'No custom renderer fallback. Report the gap; existing partial output is not verified.' }));
  process.exitCode = 2;
});
