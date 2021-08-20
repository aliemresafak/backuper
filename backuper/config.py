from pathlib import Path
from dotenv import find_dotenv, dotenv_values

env = dict(dotenv_values(find_dotenv()))

BACKUP_PATH = Path(".") / env["BACKUP_FOLDER_NAME"]
CREDENTIALS_PATH = Path(".") / env["CREDENTIALS_FILE_NAME"]

START_DATETIME_FORMAT = "%Y-%m-%d 00:00:00"
FINISH_DATETIME_FORMAT = "%Y-%m-%d 23:59:59"