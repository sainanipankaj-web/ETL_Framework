import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from config.config import DATABASE_NAME, TARGET_FILE_PATH

from validations.data_profiling import (
    generate_data_profile,
    export_profile_report
)


# =========================
# DATA PROFILING TEST
# =========================

def test_generate_data_profile():

    df = pd.read_csv("target/transformed_employees.csv")

    profile = generate_data_profile(df)

    export_profile_report(
        profile,
        "reports/profile_report.json"
    )

    assert profile["total_rows"] > 0