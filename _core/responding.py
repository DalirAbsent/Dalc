from types import FunctionType
from _core.processing import computing
from _core.frontend import shaping


def response(data: str) -> str | None:
    """
    Passes the input data to `_core.processing` function.
    If the result is a function tries to run it and then returns `None`, otherwise
    prepares the result to print by `_core.frontend` `shaping`.
    if the result is `None` returns `None`.
    """
    result = computing(data)
    
    if result is None:
        return None
    
    if type(result) is FunctionType:
        try:
            result()
            return None

        except Exception:
            answer = shaping(Exception)
            return answer
    
    answer = shaping(result)

    return answer
