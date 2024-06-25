from os import system
from _core.setting import file_viewer_command, print_input_command, is_path_exists
from _core.frontend import shaping


def view(data):
    """
    Shows files and other outputs in standard output.
    If `data` is an existing file shows the file, otherwise
    computed it in `_core.processing` module and then shows it.
    """

    if data is None:
        return None
    
    def viewer():

        if type(data) is str and is_path_exists(data):
            system(f"{file_viewer_command} {data}")

        else:
            answer = shaping(data)
            system(f"{print_input_command} '{answer}' | {file_viewer_command}")

    return viewer
