from sys import argv
from _core.processing import computing
from _core.setting import is_error
from _core.frontend import all_texts


def gather() -> tuple | None:
    """
    Handling command line arguments.
    """
    if len(argv) > 1:

        answer: list = list()

        for data in argv[1:]:
            result = computing(data.strip())

            if is_error(result):
                result = all_texts(str(result))

            answer.append(result)
        
        if len(answer) == 1:
            return answer[0]
        
        return tuple(answer)
    
    return None
