from wera import FileType, File, rule


@rule(
    description="A-3: Missing line break at end of file",
    type_filter=FileType.ALL()
)
def check(file: File):
    if file.lines[-1]:
        file.report(len(file.lines))
