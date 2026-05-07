import pandas as pd

# Read source file
df = pd.read_csv("data/source_employees.csv")

print("SOURCE DATA:")
print(df)

print("\nTOTAL RECORDS:")
print(len(df))

print("\nNULL VALUES:")
print(df.isnull().sum())

print("\n \nSalary :")
print(df["salary"].dtype)
assert df["salary"].dtype != "float64"