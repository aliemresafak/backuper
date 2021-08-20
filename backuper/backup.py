from os import path, makedirs
from pathlib import Path
from backuper.config import BACKUP_PATH

class Backup:
    def __init__(self, backup_path: Path, table_names: list[str]):
        self.backup_path = backup_path
        self.table_names = table_names 

        self._generate_folder()
    
    def _generate_folder(self):
        # Check backup folder
        if not path.exists(BACKUP_PATH):
            makedirs(BACKUP_PATH)
        