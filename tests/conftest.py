import os
import pathlib
import pytest
import subprocess


class RuleFile(pytest.File):

    def collect(self):
        yield from self.check_file("fail")
        yield from self.check_file("pass")

    def check_file(self, dir_type):
        if not os.path.isdir(f"{self.path}/{dir_type}"):
            return

        for filename in os.listdir(f"{self.path}/{dir_type}"):
            file_path = f"{self.path}/{dir_type}/{filename}"
            if os.path.isfile(file_path):
                yield RuleItem.from_parent(self, name=file_path)


class RuleItem(pytest.Item):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def runtest(self):
        out = subprocess.getoutput(
            f"vera++ --profile chaos --root src -d {self.name}"
        )
        if "fail" in self.name:
            assert out != ""

        if "pass" in self.name:
            assert out == ""


cache = set()


def pytest_collect_file(parent, file_path: pathlib.PosixPath):
    parts = file_path.parts
    if 'fixtures' in parts:
        cat, rule, *_ = parts[-4:]
        p = f"{cat}/{rule}"
        if p not in cache:
            cache.add(p)
            return RuleFile.from_parent(
                parent, path=file_path.parent.parent
            )
