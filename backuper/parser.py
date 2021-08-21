from yaml import load, Loader
from pathlib import Path
from backuper.config import *

class YamlParser:
    def __init__(self):
        self.file_path = DATABASE_CONFIG_PATH

    def parse(self) -> dict:
        try:
            with open(self.file_path, "r") as file:
                data = load(file, Loader=Loader)
                return data["database"]
        except FileNotFoundError as error:
            print(f"Config file not found, please check it")
