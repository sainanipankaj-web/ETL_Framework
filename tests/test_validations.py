import pandas as pd

# Read transformed file
df = pd.read_csv("target/transformed_employees.csv")


# =========================
# TEST ROW COUNT
# =========================

def test_row_count():
    assert len(df) == 4


# =========================
# TEST NULL SALARY
# =========================

def test_null_salary():
    for salary in df["salary"]:
        assert not pd.isnull(salary) and salary > 0

# =========================
# TEST BONUS COLUMN EXISTS
# =========================

def test_bonus_column():
    assert "bonus" in df.columns


# =========================
# TEST NAMES ARE UPPERCASE
# =========================

def test_names_uppercase():
    for name in df["name"]:
        assert name.isupper()