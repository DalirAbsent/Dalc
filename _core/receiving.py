from _core.frontend import user_input


def receive() -> str:
    """
    Gets data from user.
    Returns `0` if the data is empty.
    """
    text = user_input()

    try:
        data = input(text).strip() or "0"

    except (KeyboardInterrupt, EOFError):
        data = "exit"

    return data
