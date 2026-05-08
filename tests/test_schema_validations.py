import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from config.config import DATABASE_NAME, TARGET_FILE_PATH

from validations.schema_validations import (
    validate_expected_columns,
    validate_column_datatypes,
    validate_column_order
)


# =========================
# SCHEMA VALIDATION TESTS
# =========================

def test_validate_expected_columns():

    df = pd.read_csv(TARGET_FILE_PATH)

    expected_columns = [
        "emp_id",
        "name",
        "department",
        "salary",
        "bonus"
    ]

    validate_expected_columns(df, expected_columns)


def test_validate_column_datatypes():

    df = pd.read_csv(TARGET_FILE_PATH)

    expected_dtypes = {
        "emp_id": "int64",
        "name": "str",
        "department": "str",
        "salary": "int64",
        "bonus": "float64"
    }

    validate_column_datatypes(df, expected_dtypes)


def test_validate_column_order():

    df = pd.read_csv(TARGET_FILE_PATH)

    expected_columns = [
        "emp_id",
        "name",
        "department",
        "salary",
        "bonus"
    ]

    validate_column_order(df, expected_columns)