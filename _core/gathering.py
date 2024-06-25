from sys import argv
from _core.processing import computing
from _core.frontend import is_error
from _core.frontend import all_texts


def gather() -> tuple | None:
    """
    Handling command line arguments.
    """
    if len(argv) > 1:

        answer: list = list()

        for data in argv[1:]:
            result = str(computing(data))

            if is_error(result):
                result = all_texts(result)

            answer.append(result)
        
        return tuple(answer)
    
    return None
