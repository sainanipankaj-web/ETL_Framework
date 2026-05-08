import pandas as pd

from utils.logger import logger


# =========================
# GENERATE DATA PROFILE
# =========================

def generate_data_profile(df):

    logger.info("Generating data profile")

    profile = {}

    # =========================
    # BASIC METRICS
    # =========================

    profile["total_rows"] = len(df)

    profile["total_columns"] = len(df.columns)

    profile["columns"] = list(df.columns)

    profile["datatypes"] = df.dtypes.astype(str).to_dict()

    # =========================
    # NULL COUNTS
    # =========================

    profile["null_counts"] = df.isnull().sum().to_dict()

    # =========================
    # DUPLICATE COUNTS
    # =========================

    profile["duplicate_rows"] = int(df.duplicated().sum())

    # =========================
    # UNIQUE VALUE COUNTS
    # =========================

    unique_counts = {}

    for column in df.columns:

        unique_counts[column] = df[column].nunique()

    profile["unique_counts"] = unique_counts

    # =========================
    # NUMERIC COLUMN STATS
    # =========================

    numeric_stats = {}

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:

        numeric_stats[column] = {
            "min": float(df[column].min()),
            "max": float(df[column].max()),
            "mean": float(df[column].mean())
        }

    profile["numeric_stats"] = numeric_stats

    logger.info("Data profiling completed")

    return profile