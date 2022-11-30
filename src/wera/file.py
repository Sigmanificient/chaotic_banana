from __future__ import annotations

from enum import IntFlag, auto
from os import path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Tuple
    from vera import TokenName, TokenVector

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

        return cls.BINARY if vera.isBinary(file.full_name) else cls.OTHER


class File:
    __slots__ = ('name', 'ext', 'type', 'full_name')

    def __init__(self, filename):
        name, ext = path.splitext(filename)
        self.name = name
        self.ext = ext

        self.full_name = filename
        self.type = FileType.resolve(self)

    def __repr__(self) -> str:
        return self.full_name

    @property
    def lines(self) -> vera.StringVector:
        return vera.getAllLines(self.full_name)

    def get_all_tokens(self, token_names: List[TokenName]) -> TokenVector:
        return vera.getTokens(self.full_name, 1, 0, -1, -1, token_names)

    def get_tokens(
        self, token_names: List[TokenName],
        lines: Tuple[int, int], columns: Tuple[int, int]
    ) -> TokenVector:
        line_start, line_end = lines
        column_start, column_end = columns

        return vera.getTokens(
            self.full_name,
            line_start,
            column_start,
            line_end,
            column_end,
            token_names
        )
