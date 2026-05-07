import sqlite3
from utils.logger import logger
from config.config import DATABASE_NAME


# =========================
# CREATE DATABASE CONNECTION
# =========================

def create_connection():

    try:
        conn = sqlite3.connect(DATABASE_NAME)

        logger.info("Database connection created successfully")

        return conn

    except Exception as e:

        logger.error(f"Database connection failed: {e}")

        raise

# =========================
# EXECUTE QUERY
# =========================

def execute_query(query):

    try:
        conn = create_connection()

        cursor = conn.cursor()

        logger.info(f"Executing query: {query}")

        cursor.execute(query)

        result = cursor.fetchone()

        conn.close()

        return result

    except Exception as e:

        logger.error(f"Query execution failed: {e}")

        raise