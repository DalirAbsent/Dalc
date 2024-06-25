from os import path


# The program version
version: str = "1.1"


# The program situation
running: bool = True

# CSS status
css_status: bool = True


# Checks if a file exists
def is_path_exists(file_path) -> bool:
    return path.exists(file_path)


# Command to print input from OS
print_input_command: str = "echo"

# Command to view files
file_viewer_command: str = "less"

# History file path
history_path: str = "dalc_history"

# Creates the history file if it doesn't exist
if not is_path_exists(history_path):
    with open(history_path, "x") as fx:
        fx.close()

# The history size
history_size: int = 100


# Clear command to clear the screen
clear_command: str = "clear"


def is_error(data):
    """
    Checks is a data an error or not.
    """
    error_types = [
            str(Exception), str(SyntaxError), str(ValueError), str(NameError), str(TypeError),
            str(LookupError), str(FileNotFoundError), str(ZeroDivisionError)
                    ]

    return str(data) in error_types
