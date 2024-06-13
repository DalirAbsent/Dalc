import re
from _core.setting import version
from _core.manage_stdout import stdout
from _core.frontend import is_error
from _core.operating import operations
from _core.meta import clear, cleax, stop, restart
from _core.history import from_history, show_history, clear_history_file
from _core.viewing import view
from _core.reading import read
from _core.writing import write


def computing(data: str):
    """
    The main function for processing the data.
    """
    try:
        if "=" in data:
            try:
                compute = __calculating__(data)
                return compute
            except:
                compute = __assigning__(data)
                return compute
        
        if data.startswith("!"):
            compute = __history_cache__(data)
            return compute
        
        compute = __calculating__(data)
        return compute

    except SyntaxError:
        return SyntaxError

    except ValueError:
        return ValueError

    except TypeError:
        return TypeError
    
    except ZeroDivisionError:
        return ZeroDivisionError

    except FileNotFoundError:
        return FileNotFoundError
    
    except Exception:
        return Exception


def __calculating__(data):
    """
    Calculates `data`
    """
    calculate = eval(data, dalc_variables)
    return calculate


def __assigning__(equation: str):
    """
    Processes the assigning
    """
    def verify_variable(check_vars: tuple) -> bool:

        var_name_pattern = re.compile(r"^[a-zA-Z_]\w*$")
        meta_names = [*meta_actions.keys(), *additional_funcs.keys()]
        for check_var in check_vars:
            if not var_name_pattern.match(check_var) or check_var in meta_names:
                return False
        return True
    
    equation: list[str] = equation.split("=")
    variable: str = equation[0]
    value: str = "=".join(equation[1:])

    variables = tuple(map(lambda x: x.strip(), variable.split(",")))
    values = __calculating__(value.strip())
    
    if not verify_variable(variables):
        return NameError

    if is_error(str(values)):
        return values

    if type(values) is not tuple:
        values = tuple((values,))

    vars_len, vals_len = len(variables), len(values)

    if vars_len != vals_len and vals_len != 1:
        return SyntaxError
    
    if vals_len == 1:
        values *= vars_len

    for i in range(vars_len):
        dalc_variables[variables[i]] = values[i]
    
    answer = f"{variable}={value}"
    
    return answer


def __history_cache__(record: str):
    """
    Runs a command from the history.
    """
    command = from_history(record)
    
    if is_error(str(command)):
        return command
    
    history = map(lambda x, y: (x, y), (command,), (computing(command),))
    
    return history


def __from_file__(path: str) -> map:
    """
    Computes the data from `path`.
    """
    file_data = read(path)

    if is_error(str(file_data)):
        return file_data
    
    calculates = map(lambda data: (data, computing(data)), file_data)

    return calculates


def __help__(func):
    """
    Shows the help for `func`
    """
    result = stdout(help, (func,))
    return result


def __print__(data):
    """
    Prints the computed `data` if you use `print` command.
    """
    result = stdout(print, (data,))
    return result


meta_actions: dict = {
                    "clean": clear_history_file, "clear": clear, "cleax": cleax,
                    "exit": stop, "quit": stop, "reboot": restart, "reset": restart,
                    "restart": restart, "history": show_history
                      }

additional_funcs: dict = {
                        "help": __help__, "read": __from_file__,
                        "print": __print__, "view": view, "write": write
                          }


dalc_variables: dict = {
                    **operations, **meta_actions, **additional_funcs, "__version__": version
                    }
