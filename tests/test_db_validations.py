import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from validations.db_validations import (
    validate_db_row_count,
    validate_db_null_salary
)


# =========================
# DB ROW COUNT VALIDATION
# =========================

def test_db_row_count():

    validate_db_row_count(4)


# =========================
# DB NULL VALIDATION
# =========================

def test_db_null_salary():

    validate_db_null_salary()