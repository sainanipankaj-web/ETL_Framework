import pandas as pd

from config.config import (
    SOURCE_FILE_PATH,
    TARGET_FILE_PATH,
    TABLE_NAME
)

from utils.database_helper import create_connection
from utils.logger import logger


# =========================
# EXTRACT + TRANSFORM DATA
# =========================

def extract_transform_data():

    logger.info("ETL process started")

    # =========================
    # READ SOURCE FILE
    # =========================

    df = pd.read_csv(SOURCE_FILE_PATH)

    logger.info(
        "Source CSV loaded successfully"
    )

    # =========================
    # REMOVE NULL SALARY RECORDS
    # =========================

    df = df.dropna(subset=["salary"])

    logger.info(
        "NULL salary records removed"
    )

    # =========================
    # CONVERT NAMES TO UPPERCASE
    # =========================

    df["name"] = df["name"].str.upper()

    logger.info(
        "Names converted to uppercase"
    )

    # =========================
    # ADD BONUS COLUMN
    # =========================

    df["bonus"] = df["salary"] * 0.10

    logger.info(
        "Bonus column added"
    )

    # =========================
    # SAVE TRANSFORMED FILE
    # =========================

    df.to_csv(
        TARGET_FILE_PATH,
        index=False
    )

    logger.info(
        "Transformed CSV saved successfully"
    )

    logger.info(
        f"Total transformed records: {len(df)}"
    )

    return df


# =========================
# LOAD DATA TO DATABASE
# =========================

def load_to_database(df):

    logger.info(
        "Database load process started"
    )

    conn = create_connection()

    df.to_sql(
        TABLE_NAME,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    logger.info(
        "Data loaded into database successfully"
    )