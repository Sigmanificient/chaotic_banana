from wera import FileType, File, rule


@rule(
    description="A-3: Missing line break at end of file",
    type_filter=FileType.project()
)
def check(file: File):
    if file.lines[-1]:
        yield file, len(file.lines)
