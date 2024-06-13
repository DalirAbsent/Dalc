from os import system
from _core.setting import history_path, history_size, file_viewer_command


def recording(data: str) -> None:
    """
    Writes the input to the history in 'history_path'.
    """
    if not __is_history_form__(data):

        count = __history_count__()

        with open(history_path, "a") as fa:
            fa.write(f"{count}  {data}\n")

        __clear_history__()


def from_history(record: str):
    """
    If the input exists in the history, calls the input
    from the history, otherwise raises `LookupError`.
    If the input form isn't `__is_history_form__` raises `Exception`.
    """
    if not __is_history_form__(record):
        return Exception
    
    number = record[1:].strip()

    with open(history_path) as fr:
        lines = fr.readlines()

    for i in lines:
        count, *command = i.split()
        
        if number == count:
            command = " ".join(command)
            return command
        
    return LookupError


def show_history():
    """
    Shows the history.
    """
    system(f"{file_viewer_command} {history_path}")


def clear_history_file():
    """
    Clears the entire history file in `history_path`.
    """
    with open(history_path, "w") as fw:
        fw.write("")


def __history_count__() -> int:
    """
    Numbering the history.
    """
    with open(history_path) as fr:

        try:
            last_input = fr.readlines()[-1]
            counter = int(last_input.split()[0]) + 1
        except IndexError:
            counter = 1

    return counter


def __clear_history__() -> None:
    """
    Clears the history if its size is greater than `history_size`.
    """
    with open(history_path) as fr:
        lines = fr.readlines()

    line_count = len(lines)
    
    if line_count > history_size:
        fw = open(history_path, "w")
        lines.pop(0)
        fw.writelines(lines)
        fw.close()
                

def __is_history_form__(data: str) -> bool:
    """
    Checks if the input, requests a record from the history.
    """
    if data.startswith("!") and data[1:].strip().isdigit():
        return True
    
    return False
