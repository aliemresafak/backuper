from datetime import datetime
from os import path, makedirs, system
from pathlib import Path
from backuper.config import BACKUP_PATH
from .parser import YamlParser

class Backup:
    def __init__(self, data: YamlParser.parse ):
        self.backup_path = BACKUP_PATH
        self.data = data
        self._generate_folder()
    
    def _generate_folder(self):
        # Check backup folder
        if not path.exists(BACKUP_PATH):
            makedirs(BACKUP_PATH)
        for db_name in self.data:
            if not path.exists(BACKUP_PATH / db_name):
                makedirs(BACKUP_PATH / db_name)
            for table_name in self.data[db_name]:
                if not path.exists(BACKUP_PATH / db_name / table_name):
                    makedirs(BACKUP_PATH / db_name / table_name)
    
    def _backup(self):
        for db_name in self.data:
            for table_name in self.data:
                start_time = datetime.now().strftime(START_DATETIME_FORMAT)
                finish_time = datetime.now().strftime(FINISH_DATETIME_FORMAT)
                export_file_path = BACKUP_PATH / db_name / table_name
                command = f"""mysqldump --extras-default-file {db_name} {table_name} --where="timestamp between '{start_time}' and '{finish_datetime}' > {export_file_path}"""
                system(command)
