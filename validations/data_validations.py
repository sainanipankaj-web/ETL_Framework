import pandas as pd


# =========================
# VALIDATE NULL VALUES
# =========================

def validate_nulls(df, column_name):
    null_count = df[column_name].isnull().sum()

    assert null_count == 0, (
        f"NULL values found in column '{column_name}'. "
        f"NULL count: {null_count}"
    )


# =========================
# VALIDATE COLUMN EXISTS
# =========================

def validate_column_exists(df, column_name):

    assert column_name in df.columns, (
        f"Column '{column_name}' does not exist"
    )


# =========================
# VALIDATE ROW COUNT
# =========================

def validate_row_count(df, expected_count):

    actual_count = len(df)

    assert actual_count == expected_count, (
        f"Row count mismatch. "
        f"Expected: {expected_count}, Actual: {actual_count}"
    )


# =========================
# VALIDATE UPPERCASE
# =========================

def validate_uppercase(df, column_name):

    for value in df[column_name]:

        assert value.isupper(), (
            f"Value '{value}' is not uppercase"
        )

# =========================
# VALIDATE DUPLICATES
# =========================

def validate_no_duplicates(df, column_name):

    duplicate_count = df[column_name].duplicated().sum()

    assert duplicate_count == 0, (
        f"Duplicates found in column '{column_name}'. "
        f"Duplicate count: {duplicate_count}"
    )