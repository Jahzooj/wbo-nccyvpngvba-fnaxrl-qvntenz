from dotenv import load_dotenv
import logging
import os
from pythonjsonlogger import jsonlogger

load_dotenv()

DB_ENDPOINT = os.getenv('DB_ENDPOINT')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DATABASE_URL = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}'

ENV = os.getenv('ENV', 'dev')

# ---
logger = logging.getLogger()

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)