from types import FunctionType
from _core.setting import css_status


def user_input() -> str:
    """
    Returns the user's input text.
    """
    constant_text = all_texts("user_input")
    text = __css__(constant_text, 33)

    return text


def shaping(result):
    """
    Specifies type of the data to pass it to the
    appropriate function and then returns the result.
    """
    
    if type(result) is map:
        answer = __file_output__(result)
        return answer
    
    answer = __user_output__(str(result))
    return answer
    

def user_quit_text() -> str:
    """
    User text on exit.
    """
    constant_text = all_texts("quit_text")
    text = __css__(constant_text)

    return text


def is_error(data: str):
    """
    Checks is a data an error or not.
    """
    error_types = [
            str(Exception), str(SyntaxError), str(ValueError), str(NameError), str(TypeError),
            str(LookupError), str(FileNotFoundError), str(ZeroDivisionError)
                    ]

    return data in error_types


def all_texts(text) -> str:
    """
    All texts
    """
    texts: dict = {

        # Constant texts
        "user_input": "[In]: ",
        "user_output": "[Out]: ",

        # Errors texts
        "constant_error_text": "Error: ",
        str(SyntaxError): "Invalid syntax",
        str(ValueError): "Over of value limit",
        str(NameError): "Invalid variable name",
        str(TypeError): "Function argument error",
        str(LookupError): "History not found",
        str(FileNotFoundError): "No such file or directory",
        str(ZeroDivisionError): "Division by zero is undefined",
        str(Exception): "Invalid input",

        # Other texts
        "quit_text": ""

                    }
    
    return texts[text]


def __css__(text, color_out=0, color_in=0, style_out=0, style_in=3) -> str:
    """
    Coloring and styling the input.
    """
    if css_status:
        color_sys = f"\033[{color_out}m"
        color_usr = f"\033[{color_in}m"
        style_sys = f"\033[{style_out}m"
        style_usr = f"\033[{style_in}m"

        text = f"{style_sys}{color_sys}{text}{color_usr}{style_usr}"

        return text
    
    else:
        return text


def __user_output__(data: str) -> str:
    """
    Gets a text data and prepares it to print according to the data type.
    If the data is error, it is different from the non-error data.
    """
    constant_text = all_texts("user_output")

    if is_error(data):
        text = __css__(constant_text, 31)
        constant_error_text = all_texts("constant_error_text")
        error_text = all_texts(data)
        data = constant_error_text + error_text
    
    else:
        text = __css__(constant_text, 32)

    answer = f"{text}{data}"

    if answer[-1] != "\n":
        answer += "\n"

    return answer


def __file_output__(data: map) -> str:
    """
    Gets a `map` data type and prepares it to print.
    """
    data = tuple(data)
    
    answer: str = str()

    for equation, calculate in data:

        if type(calculate) is FunctionType:
            calculate()
            continue
        
        if calculate is None:
            answer += user_input() + equation
            continue

        input_text = user_input() + equation
        output_text = __user_output__(str(calculate)) + "\n"

        if input_text[-1] != "\n":
            input_text += "\n"

        answer += input_text + output_text
    
    return answer.removesuffix("\n")
