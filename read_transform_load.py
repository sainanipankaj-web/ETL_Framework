import pandas as pd

# =========================
# READ SOURCE FILE
# =========================

df = pd.read_csv("data/source_employees.csv")

print("SOURCE DATA:")
print(df)

# =========================
# TOTAL RECORDS
# =========================

print("\nTOTAL RECORDS:")
print(len(df))

# =========================
# NULL VALIDATION
# =========================

print("\nNULL VALUES:")
print(df.isnull().sum())

# =========================
# REMOVE NULL SALARY RECORDS
# =========================

df = df.dropna(subset=["salary"])

print("\nAFTER REMOVING NULL SALARY:")
print(df)

# =========================
# CONVERT NAMES TO UPPERCASE
# =========================

df["name"] = df["name"].str.upper()

print("\nAFTER CONVERTING NAMES TO UPPERCASE:")
print(df)

# =========================
# ADD BONUS COLUMN
# BONUS = 10% OF SALARY
# =========================

df["bonus"] = df["salary"] * 0.10

print("\nAFTER ADDING BONUS COLUMN:")
print(df)

# =========================
# CONVERT SALARY TO INTEGER
# =========================

df["salary"] = df["salary"].astype(int)

# =========================
# SAVE TRANSFORMED FILE
# =========================

df.to_csv("target/transformed_employees.csv", index=False)

nf = pd.read_csv("target/transformed_employees.csv")

print("\nREAD BACK TRANSFORMED FILE:")
print(nf)

print("\nTRANSFORMED FILE SAVED SUCCESSFULLY")