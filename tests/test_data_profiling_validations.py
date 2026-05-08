import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pandas as pd
from config.config import DATABASE_NAME, TARGET_FILE_PATH

from validations.data_profiling import (
    generate_data_profile
)

# =========================
# DATA PROFILING TEST
# =========================

def test_generate_data_profile():

    df = pd.read_csv(TARGET_FILE_PATH)
    profile = generate_data_profile(df)

    print("\nDATA PROFILE:")
    print(profile)

    assert profile["total_rows"] > 0, "Total rows should be greater than 0"