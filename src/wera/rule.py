import vera

from wera import FileType, File


def rule(description: str, type_filter: FileType):

    def decorator(func):
        File.set_reported_rule(description)

        for filepath in vera.getSourceFileNames():
            file = File(filepath)

            if file.type & type_filter:
                func(file)

    return decorator
