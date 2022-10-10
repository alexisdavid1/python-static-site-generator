from msilib.schema import Directory
from pathlib import path


class Site:

    def __init__(self, source, dest):
        self.source = path(source)
        self.dest = path(dest)

    def create_dir(self, path):
        directory = self.dest/path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path == self.create_dir.directory:
                return self.create_dir(path)
