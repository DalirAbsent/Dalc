from _core.setting import is_path_exists


def read(path: str):
    """
    If `path` is an existing file, reads the file and
    prepares it to compute, otherwise returns `FileNotFoundError`.
    """
    if is_path_exists(path):
        with open(path) as fr:
            lines: list[str] = fr.readlines()
            fr.close()

        data = tuple(filter(lambda x: x.strip(), lines))
        return data

    return FileNotFoundError
