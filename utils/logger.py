import logging
import os
from config.config import LOG_FILE_PATH


# Create logs folder if not exists
os.makedirs("logs", exist_ok=True)

# Create logger
logger = logging.getLogger("ETL_Framework")

# Prevent duplicate handlers
if not logger.handlers:

    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(LOG_FILE_PATH)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)