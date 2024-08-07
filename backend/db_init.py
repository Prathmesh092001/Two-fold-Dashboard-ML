import os
import pandas as pd
from sqlalchemy import create_engine
from config import Config
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    # Initialize the database connection
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    logger.info("Connected to PostgreSQL successfully")
    connection.close()
except Exception as e:
    logger.error(f"Failed to connect to PostgreSQL: {e}")
    raise

# Path to the data directory at the project root
data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

# List of data files
files = ['5308.xls', '5329.xls']

# Check files in the data directory
available_files = os.listdir(data_dir)
logger.info(f"Files in data directory: {available_files}")

for file in files:
    file_path = os.path.join(data_dir, file)
    if not os.path.exists(file_path):
        logger.error(f"File {file_path} not found.")
        continue
    
    df = pd.read_excel(file_path, sheet_name=None)
    for sheet_name, sheet_data in df.items():
        sheet_data.to_sql(sheet_name, engine, if_exists='replace', index=False)

logger.info("Data loaded into PostgreSQL successfully")
