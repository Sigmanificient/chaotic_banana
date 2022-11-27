from __future__ import annotations
from enum import IntFlag, auto
from os import path

import vera


class FileType(IntFlag):
    BINARY = auto()
    HEADER = auto()
    SOURCE = auto()
    MAKEFILE = auto()
    OTHER = auto()

    @classmethod
    def ALL(cls) -> FileType:
        return (
            cls.BINARY | cls.HEADER
            | cls.SOURCE | cls.MAKEFILE
            | cls.OTHER
        )


class File:
    __report_message = "not set"

    def __init__(self, filename):
        name, ext = path.splitext(filename)
        self.name = name
        self.ext = ext

        self.type = self.__get_file_type(name, ext)
        self.full_name = filename

    @classmethod
    def set_reported_rule(cls, message: str):
        cls.__report_message = message

    @staticmethod
    def __get_file_type(name: str, ext: str) -> FileType:
        match (name, ext):
            case ("Makefile", _):
                return FileType.MAKEFILE
            case (_, ".h"):
                return FileType.HEADER
            case (_, ".c"):
                return FileType.SOURCE
            case (_, _):
                return FileType.OTHER

    def report(self, line: int):
        vera.report(self.full_name, line, self.__report_message)

    def __repr__(self) -> str:
        return self.full_name

    @property
    def lines(self) -> vera.StringVector:
        return vera.getAllLines(self.full_name)




