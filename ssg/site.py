from msilib.schema import Directory
from pathlib import Path

from conftest import Parser


class Site:

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest/path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                return self.create_dir(path)
            elif path is file:
                self.run_parser(path)

    def load_parser(self, extension):
        for parser in self.parsers:
            if extension is Parser.valid_extension():
                return parser

    def run_parser(self, path):
        parser = self.load_parser(path.suffix)
        if parser != None:
            return Parser.parse()
        else:
            NotImplemented
