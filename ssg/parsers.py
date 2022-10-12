from importlib.resources import path
from typing import List
from pathlib import Path
from shutil import *


class Parser:
    extensions = [List[str]]

    def valid_extension(self, extension):
        return True if extension in Parser.extensions else False

    def parse(self, Path(path), Path(source), Path(dest)):
        raise NotImplementedError

    def read(self, path):
        with open("path") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path = self.dest/path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(self.content)

    def copy(self, path, source, dest):
        copy2(path, dest/source.path)


class ResourceParser:
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, Path(path), Path(source), Path(dest)):
        super().copy()
