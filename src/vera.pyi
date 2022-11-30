from typing import List, Generic, TypeVar, Literal, Iterator

T = TypeVar('T')


TokenName = Literal[
    "and", "andand", "assign", "andassign", "or", "orassign", "xor",
    "xorassign", "comma", "colon", "divide", "divideassign", "dot", "dotstar",
    "ellipsis", "equal", "greater", "greaterequal", "leftbrace", "less",
    "lessequal", "leftparen", "leftbracket", "minus", "minusassign",
    "minusminus", "percent", "percentassign", "not", "notequal", "oror",
    "plus", "plusassign", "plusplus", "arrow", "arrowstar", "question_mark",
    "rightbrace", "rightparen", "rightbracket", "colon_colon", "semicolon",
    "shiftleft", 'shiftleftassign', "shiftright", "shiftrightassign", "star",
    "compl", "starassign", "asm", "auto", "bool", "false", "true", "break",
    "case", "catch", "char", "class", "const", "constcast", "continue",
    "default", "delete", "do", "double", "dynamiccast", "else", "enum",
    "explicit", "export", "extern", "float", "for", "friend", "goto", "if",
    "inline", "int", "long", "mutable", "namespace", "new", "operator",
    "private", "protected", "public", "register", "reinterpretcast", "return",
    "short", "signed", "sizeof", "static", "staticcast", "struct", "switch",
    "template", "this", "throw", "try", "typedef", "typeid", "typename",
    "union", "unsigned", "using", "virtual", "void", "volatile", "wchart",
    "while", "pp_define", "pp_if", "pp_ifdef", "pp_ifndef", "pp_else",
    "pp_elif", "pp_endif", "pp_error", "pp_line", "pp_pragma", "pp_undef",
    "pp_warning", "identifier", "octalint", "decimalint", "hexaint", "intlit",
    "longintlit", "floatlit", "ccomment", "cppcomment", "charlit", "stringlit",
    "contline", "space", "space2", "newline", "pound_pound", "pound", "any",
    "pp_include", "pp_qheader", "pp_hheader", "eof", "eoi", "pp_number",
    "msext_int8", "msext_int16", "msext_int32", "msext_int64", "msext_based",
    "msext_declspec", "msext_cdecl", "msext_fastcall", "msext_stdcall",
    "msext_try", "msext_except", "msext_finally", "msext_leave",
    "msext_inline", "msext_asm", "msext_region", "msext_endregion", "import"
]

class Token:
    column: int
    file: str
    line: int
    name: str
    raw: str
    type: str
    value: str


class _Vector(Generic[T]):

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> T:  ...
    def __setitem__(self, index: int, value: T) -> None: ...
    def __iter__(self) -> Iterator[T]: ...

    def append(self, value: T) -> None: ...
    def extend(self, values: List[T]) -> None: ...


class TokenVector(_Vector[Token]):
    ...


class StringVector(_Vector[str]):
    ...

def getAllLines(filepath: str) -> StringVector: ...

def getLine(filepath: str, line: int) -> str: ...

def getLineCount(filepath: str) -> int: ...

def getParameter(filepath: str, default_value: str) -> str: ...

def getSourceFileNames() -> StringVector: ...

def getTokens(
    filename: str,
    from_line: int,
    from_column: int,
    to_line: int,
    to_column: int,
    token_filter: List[TokenName],
) -> TokenVector: ...

def isBinary(filepath: str) -> bool: ...

def report(filepath: str, line: int, rule: str) -> None: ...

__all__ = (
    'Token',
    'TokenName',
    'TokenVector',
    'StringVector',
    'getAllLines',
    'getLine',
    'getLineCount',
    'getParameter',
    'getSourceFileNames',
    'getTokens',
    'isBinary',
    'report'
)
