import pandas as pd
from utils.database_helper import create_connection
from utils.logger import logger
from config.config import TABLE_NAME, TARGET_FILE_PATH

# Read source file
df = pd.read_csv(TARGET_FILE_PATH)

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
    TABLE_NAME,
    conn,
    if_exists="replace",
    index=False
)

logger.info("DATA LOADED INTO SQLITE DATABASE")

conn.close()