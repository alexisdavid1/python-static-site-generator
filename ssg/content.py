import re
from yaml import load
from yaml import FullLoader
from _collections_abc import Mapping


class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _ = Content.__regex.re.split(string, 2)
        fm = Content.__regex.re.split(string, 2)
        content = Content.__regex.re.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(self.metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {"content": content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        if self.data_has_key(type):
            return self.data["type"]
        else:
            return None
