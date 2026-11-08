"""Pure manifest checks for read-only domain-level IST evaluation."""
CONTRACT_ID = "m1_bpmn_ist_evaluation/0.3.0"


def artifact_refs(state):
    return [{key: item[key] for key in ("artifact_id", "path", "sha256")}
            for item in state["artifacts"]]


def validate(state):
    # Called after strict schema validation. No file access and no text classifier.
    errors = []

    def error(code, path, message):
        errors.append(dict(code=code, path=path, message=message))

    def index(field, key):
        result = {}
        for i, item in enumerate(state[field]):
            if item[key] in result:
                error("DUPLICATE_ID", f"/{field}/{i}/{key}", "Kennung ist nicht eindeutig.")
            result[item[key]] = item
        return result

    artifacts = index("artifacts", "artifact_id")
    models = index("models", "model_id")
    sources = index("sources", "source_id")
    index("issues", "issue_id")
    index("checks", "check_id")
    used = set()
    for i, artifact in enumerate(state["artifacts"]):
        if artifact["origin"] == "derived_preview" and artifact["kind"] not in {"png", "svg"}:
            error("GENERATED_MODEL", f"/artifacts/{i}", "Nur Vorschauen dürfen abgeleitet sein; keine Modellgenerierung.")
    for i, source in enumerate(state["sources"]):
        aid = source["artifact_id"]
        if aid not in artifacts:
            error("SOURCE_REF", f"/sources/{i}", "Quellenbeleg fehlt.")
        used.add(aid)
    for i, model in enumerate(state["models"]):
        path = f"/models/{i}"
        model_artifacts = [artifacts[a] for a in model["artifact_ids"] if a in artifacts]
        if len(model_artifacts) != len(model["artifact_ids"]):
            error("ARTIFACT_BINDING", path, "Modelldatei fehlt.")
        used.update(model["artifact_ids"])
        bpmn = model["bpmn_artifact_id"]
        xml_files = {a["artifact_id"] for a in model_artifacts if a["kind"] == "bpmn"}
        if (bpmn is None and xml_files) or (bpmn is not None and xml_files != {bpmn}):
            error("BPMN_BINDING", path, "BPMN-Zuordnung ist unvollständig oder mehrdeutig.")
        if not any(a["kind"] in {"bpmn", "png", "svg", "pdf"} for a in model_artifacts):
            error("MODEL_INPUT", path, "Mindestens ein Modell oder lesbarer Export erforderlich.")
        images = any(a["kind"] in {"png", "svg", "pdf"} for a in model_artifacts)
        if not images and model["image_status"] != "not_available":
            error("IMAGE_STATUS", path, "Ohne Export keine Bildzuordnung bestätigen.")
        if images and model["image_status"] == "not_available":
            error("IMAGE_STATUS", path, "Vorhandenen Export nicht als fehlend deklarieren.")
        if model["image_status"] in {"matched", "mismatch"} and (bpmn is None or not model["image_evidence"].strip()):
            error("IMAGE_EVIDENCE", path, "XML-/Bildabgleich benötigt XML und tatsächlichen Inhaltsbeleg.")
        if bpmn is None and not model["limitations"]:
            error("MODEL_LIMITATION", path, "Export ohne XML muss als Teilprüfung gekennzeichnet sein.")
    if used != set(artifacts):
        error("UNREFERENCED_ARTIFACT", "/artifacts", "Alle Dateien einem Modell oder einer Quelle zuordnen.")
    for field in ("issues", "checks"):
        for i, item in enumerate(state[field]):
            path = f"/{field}/{i}"
            model = models.get(item["model_id"])
            if model is None or item["model_revision"] != model["model_revision"]:
                error("MODEL_REVISION", path, "Befund/Prüfung gehört nicht zur aktuellen Modellfassung.")
                continue
            if field == "issues":
                if item["category"] == "error" and (item["certainty"] != "proven" or not item["evidence"]):
                    error("UNPROVEN_ERROR", path, "Belegter Fehler benötigt Evidenz und Sicherheit belegt.")
                if item["category"] == "error" and item["rule_kind"] in {"modeling_recommendation", "clarification"}:
                    error("ERROR_RULE", path, "Empfehlung oder Klärungsbedarf allein ist kein belegter Fehler.")
                if item["rule_kind"] == "understandability_criterion" and item["dimension"] != "pragmatics":
                    error("RULE_DIMENSION", path, "Verständlichkeitskriterien gehören zur Pragmatik.")
                for evidence in item["evidence"]:
                    valid = (evidence["ref_id"] in sources if evidence["basis"] == "source"
                             else evidence["ref_id"] == model["model_id"])
                    if not valid:
                        error("EVIDENCE_REF", path, "Evidenz verweist auf unbekannte Quelle oder anderes Modell.")
            else:
                if not set(item["artifact_ids"]).issubset(model["artifact_ids"]):
                    error("CHECK_ARTIFACT", path, "Prüfung verweist auf Dateien eines anderen Modells.")
                if item["status"] == "not_assessable" and not item["limitations"]:
                    error("CHECK_LIMITATION", path, "Nicht beurteilbare Prüfung benötigt eine konkrete Grenze.")
                if item["status"] != "not_checked" and (item["performed_by"] == "none" or not item["evidence"].strip()):
                    error("CHECK_EVIDENCE", path, "Tatsächlicher Prüfer und Prüfumfang erforderlich.")
                if item["kind"] == "visual" and item["status"] in {"partial", "checked"}:
                    has_export = any(artifacts[a]["kind"] in {"png", "svg", "pdf"}
                                     for a in item["artifact_ids"] if a in artifacts)
                    if not has_export or model["image_status"] == "mismatch":
                        error("VISUAL_INPUT", path, "Sichtprüfung benötigt zugeordneten lesbaren Export.")
                    if item["status"] == "checked" and model["bpmn_artifact_id"] is not None and model["image_status"] != "matched":
                        error("VISUAL_NOT_MATCHED", path, "Vollständig durchgeführte Sichtprüfung erfordert den belegten XML-/Bildabgleich.")
    return errors
