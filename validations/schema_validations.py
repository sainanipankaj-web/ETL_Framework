import pandas as pd

from utils.logger import logger


# =========================
# VALIDATE EXPECTED COLUMNS
# =========================

def validate_expected_columns(df, expected_columns):

    logger.info("Validating expected columns")

    actual_columns = list(df.columns)

    missing_columns = []

    for column in expected_columns:

        if column not in actual_columns:
            missing_columns.append(column)

    assert len(missing_columns) == 0, (
        f"Missing columns found: {missing_columns}"
    )

    logger.info("Expected column validation passed")


# =========================
# VALIDATE COLUMN DATATYPES
# =========================

def validate_column_datatypes(df, expected_dtypes):

    logger.info("Validating column datatypes")

    datatype_mismatches = []

    for column, expected_dtype in expected_dtypes.items():

        actual_dtype = str(df[column].dtype)

        if actual_dtype != expected_dtype:

            datatype_mismatches.append(
                f"{column}: Expected={expected_dtype}, Actual={actual_dtype}"
            )

    assert len(datatype_mismatches) == 0, (
        f"Datatype mismatches found: {datatype_mismatches}"
    )

    logger.info("Datatype validation passed")


# =========================
# VALIDATE COLUMN ORDER
# =========================

def validate_column_order(df, expected_columns):

    logger.info("Validating column order")

    actual_columns = list(df.columns)

    assert actual_columns == expected_columns, (
        f"Column order mismatch. "
        f"Expected={expected_columns}, Actual={actual_columns}"
    )

    logger.info("Column order validation passed")