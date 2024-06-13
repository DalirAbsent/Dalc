from os import system, execl
from sys import executable, argv
from _core.setting import clear_command
from _core.frontend import user_quit_text


def clear():
    """
    Clears the screen.
    """
    system(clear_command)


def stop():
    """
    Prints the user exit text, then exits the program.
    """
    print(user_quit_text())
    exit()


def restart():
    """
    Restarts the program.
    """
    clear()
    execl(executable, executable, *argv)


def cleax():
    """
    Clears the screen, prints the user exit text, then exits the program.
    """
    clear()
    stop()
