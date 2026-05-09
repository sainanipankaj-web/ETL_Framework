import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pipelines.etl_pipeline import (
    extract_transform_data,
    load_to_database
)

from utils.logger import logger

from utils.audit_helper import (
    start_audit,
    end_audit,
    export_audit_report
)


# =========================
# MAIN PIPELINE EXECUTION
# =========================

def run_pipeline():

    # START AUDIT
    audit_data = start_audit(
        "employee_etl_pipeline"
    )

    try:

        logger.info(
            "Pipeline execution started"
        )

        # =========================
        # TASK 1 - EXTRACT + TRANSFORM
        # =========================

        df = extract_transform_data()

        logger.info(
            "Extract and transform completed"
        )

        # =========================
        # TASK 2 - LOAD DATABASE
        # =========================

        load_to_database(df)

        logger.info(
            "Database load completed"
        )

        # =========================
        # PIPELINE SUCCESS AUDIT
        # =========================

        audit_data = end_audit(
            audit_data=audit_data,
            total_records=len(df),
            failed_records=0,
            status="SUCCESS"
        )

    except Exception as e:

        logger.error(
            f"Pipeline execution failed: {e}"
        )

        # =========================
        # PIPELINE FAILURE AUDIT
        # =========================

        audit_data = end_audit(
            audit_data=audit_data,
            total_records=0,
            failed_records=1,
            status="FAILED"
        )

    finally:

        # =========================
        # EXPORT AUDIT REPORT
        # =========================

        export_audit_report(
            audit_data,
            "reports/audit_report.json"
        )

        logger.info(
            "Audit report generated successfully"
        )


# =========================
# ENTRY POINT
# =========================

if __name__ == "__main__":

    run_pipeline()