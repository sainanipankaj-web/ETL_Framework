import pandas as pd

from utils.database_helper import create_connection

from config.config import TARGET_FILE_PATH, TABLE_NAME


# =========================
# VALIDATE SOURCE VS TARGET COUNT
# =========================

def validate_source_target_count():

    # Read source CSV
    source_df = pd.read_csv(TARGET_FILE_PATH)

    source_count = len(source_df)

    # Read target DB
    conn = create_connection()

    target_df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    target_count = len(target_df)

    conn.close()

    assert source_count == target_count, (
        f"Source and Target count mismatch. "
        f"Source: {source_count}, Target: {target_count}"
    )

# =========================
# VALIDATE SALARY MATCH
# =========================

def validate_salary_match():

    # Read source CSV
    source_df = pd.read_csv(TARGET_FILE_PATH)

    # Read target DB
    conn = create_connection()

    target_df = pd.read_sql_query(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    # Merge source and target
    merged_df = source_df.merge(
        target_df,
        on="emp_id",
        suffixes=("_source", "_target")
    )

    # Compare salary
    mismatches = merged_df[
        merged_df["salary_source"] != merged_df["salary_target"]
    ]

    assert mismatches.empty, (
        f"Salary mismatches found:\n{mismatches}"
    )