from __future__ import annotations

from wera import FileType, rule

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wera import File
    from typing import Iterator, Tuple


@rule(
    description="(Major) C-3: Use of forbidden goto statement",
    type_filter=FileType.source()
)
def check(file: File) -> Iterator[Tuple[File, int]]:
    for goto_token in file.get_all_tokens(['goto']):
        yield file, goto_token.line
