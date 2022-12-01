import vera

from wera import FileType, File


def rule(description: str, type_filter: FileType):
    def decorator(func):

        for filepath in vera.getSourceFileNames():
            file = File(filepath)

            if not file.type & type_filter:
                continue

            for file, line in func(file):
                vera.report(file.name, line, description)

    return decorator
