import re
from _core.setting import is_path_exists
from _core.frontend import is_error, shaping


def write(data, path) -> None:
    """
    If `path` is an existing file, writes the data in it, otherwise
    creates the file and then writes the data in it.
    If path has undefined directory returns `FileNotFoundError`.
    If `data` is an error returns it without writing it.
    """

    if is_error(str(data)):
        return data
    
    try:
        if not is_path_exists(path):
            with open(path, "x") as fx:
                fx.close()
        
    except FileNotFoundError:
        return FileNotFoundError
    
    answer = shaping(data)

    color_format = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
    answer = color_format.sub("", answer)

    with open(path, "w") as fw:
        fw.write(answer)
