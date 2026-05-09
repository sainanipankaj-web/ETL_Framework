from datetime import datetime
import json

from utils.logger import logger


# =========================
# START AUDIT
# =========================

def start_audit(pipeline_name):

    audit_data = {
        "pipeline_name": pipeline_name,
        "start_time": str(datetime.now()),
        "status": "RUNNING"
    }

    logger.info(f"Pipeline started: {pipeline_name}")

    return audit_data


# =========================
# END AUDIT
# =========================

def end_audit(
    audit_data,
    total_records,
    failed_records,
    status
):

    end_time = datetime.now()

    start_time = datetime.fromisoformat(
        audit_data["start_time"]
    )

    duration = (end_time - start_time).total_seconds()

    audit_data["end_time"] = str(end_time)

    audit_data["duration_seconds"] = duration

    audit_data["total_records"] = total_records

    audit_data["failed_records"] = failed_records

    audit_data["status"] = status

    logger.info(
        f"Pipeline completed with status: {status}"
    )

    return audit_data


# =========================
# EXPORT AUDIT REPORT
# =========================

def export_audit_report(
    audit_data,
    output_path
):

    with open(output_path, "w") as json_file:

        json.dump(audit_data, json_file, indent=4)

    logger.info(
        f"Audit report exported: {output_path}"
    )