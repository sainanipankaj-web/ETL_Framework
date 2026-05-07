import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd

from validations.data_validations import (
    validate_no_duplicates,
    validate_nulls,
    validate_column_exists,
    validate_row_count,
    validate_uppercase,
)


# Read transformed file
df = pd.read_csv("target/transformed_employees.csv")


# =========================
# TEST ROW COUNT
# =========================

def test_row_count():
    validate_row_count(df, 4)


# =========================
# TEST NULL SALARY
# =========================

def test_null_salary():
    validate_nulls(df, "salary")


# =========================
# TEST BONUS COLUMN EXISTS
# =========================

def test_bonus_column():
    validate_column_exists(df, "bonus")


# =========================
# TEST NAMES ARE UPPERCASE
# =========================

def test_names_uppercase():
    validate_uppercase(df, "name")

def test_no_duplicate_emp_id():

    validate_no_duplicates(df, "emp_id")