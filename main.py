import pandas as pd
from utils.database_helper import create_connection
from utils.logger import logger

# Read source file
df = pd.read_csv("target/transformed_employees.csv")

print("SOURCE DATA:")
print(df)

print("\nTOTAL RECORDS:")
print(len(df))

print("\nNULL VALUES:")
print(df.isnull().sum())

# =========================
# LOAD DATA INTO SQLITE DB
# =========================

conn = create_connection()

df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)

logger.info("DATA LOADED INTO SQLITE DATABASE")

conn.close()