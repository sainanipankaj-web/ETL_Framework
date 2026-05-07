from utils.database_helper import execute_query
from config.config import TABLE_NAME

# =========================
# VALIDATE ROW COUNT
# =========================

def validate_db_row_count(expected_count):

    query = f"SELECT COUNT(*) FROM {TABLE_NAME}"

    result = execute_query(query)

    actual_count = result[0]

    assert actual_count == expected_count, (
        f"DB row count mismatch. "
        f"Expected: {expected_count}, Actual: {actual_count}"
    )


# =========================
# VALIDATE NULL SALARY
# =========================

def validate_db_null_salary():

    query = f"""
    SELECT COUNT(*)
    FROM {TABLE_NAME}
    WHERE salary IS NULL
    """

    result = execute_query(query)

    null_count = result[0]

    assert null_count == 0, (
        f"NULL salaries found in DB. "
        f"NULL count: {null_count}"
    )