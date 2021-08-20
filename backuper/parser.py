from yaml import load, Loader
from pathlib import Path

class YamlParser:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def parse(self):
        try:
            with open(self.file_path, "r") as file:
                data = load(file, Loader=Loader)
                return data
            ...
        except FileNotFoundError as error:
            print(f"Config file not found, please check it")