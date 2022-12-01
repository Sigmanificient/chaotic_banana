from __future__ import annotations

from wera import FileType, rule

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wera import File
    from typing import Final, Iterator, Tuple


TAB_SIZE: Final[int] = 4


@rule(
    description="(Major) F-3: Exceeding the 80 column limit",
    type_filter=FileType.source(),
)
def check(file: File) -> Iterator[Tuple[File, int]]:
    for idx, line in enumerate(file.lines):
        line_no_tab = line.replace("\t", " " * TAB_SIZE)

        if len(line_no_tab) > 80:
            yield file, idx
