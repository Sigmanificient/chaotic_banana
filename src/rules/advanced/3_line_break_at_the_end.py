from __future__ import annotations

from wera import FileType, rule

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wera import File
    from typing import Iterator, Tuple


@rule(
    description="(Minor) A-3: Missing line break at end of file",
    type_filter=FileType.project(),
)
def check(file: File) -> Iterator[Tuple[File, int]]:
    if file.lines[-1]:
        yield file, len(file.lines)
