from __future__ import annotations

from pathlib import Path
from enum import IntFlag, auto
from os import path

import vera


class FileType(IntFlag):
    BINARY = auto()
    HEADER = auto()
    C = auto()
    MAKEFILE = auto()
    OTHER = auto()

    @classmethod
    def all(cls) -> FileType:
        return cls.BINARY | cls.HEADER | cls.C | cls.MAKEFILE | cls.OTHER

    @classmethod
    def source(cls) -> FileType:
        return cls.HEADER | cls.C

    @classmethod
    def project(cls) -> FileType:
        return cls.MAKEFILE | cls.HEADER | cls.C

    @classmethod
    def resolve(cls, file: File) -> FileType:
        if file.ext == '.h':
            return cls.HEADER
        if file.ext in '.c':
            return cls.C
        if file.name == 'Makefile':
            return cls.MAKEFILE

        return cls.BINARY if vera.isBinary(file.name) else cls.OTHER


class File:
    __slots__ = ('name', 'ext', 'type', 'full_name')

    def __init__(self, filename):
        name, ext = path.splitext(filename)
        self.name = name
        self.ext = ext

        self.type = FileType.resolve(self)
        self.full_name = filename

    def __repr__(self) -> str:
        return self.full_name

    @property
    def lines(self) -> vera.StringVector:
        return vera.getAllLines(self.full_name)
