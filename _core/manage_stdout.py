import sys
from io import StringIO


def stdout(func, func_input: tuple):
    """
    Controls the standard output.
    """
    sys.stdout = StringIO()
    func(*func_input)
    result = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    
    return result
