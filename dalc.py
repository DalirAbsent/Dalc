import readline
from _core.setting import running
from _core.receiving import receive
from _core.responding import response
from _core.history import recording
from _core.gathering import gather


def main() -> None:
    """
    The main function to starts Dalc.
    Gets the data from `_core.receiving`, saves it in the history
    then passes it to `_core.responding` `response`, to get
    a result for printing.
    if the data is `None` prints nothing.
    """
    data = receive()

    recording(data)
    result = response(data)
    if result is not None:
        print(result)


cli_gather = gather()
if cli_gather:
    print(cli_gather)
    running = False


if __name__ == "__main__":
    while running:
        main()
