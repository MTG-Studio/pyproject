from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """декоратор log автоматически регистрирует детали выполнения функций, такие как время вызова, имя функции,
    передаваемые аргументы, результат выполнения и информация об ошибках.
    Это позволяет обеспечить более глубокий контроль и анализ поведения программы в процессе ее выполнения.

    Пример использования:
        @log(filename="mylog.txt")
        def my_function(x, y):
            return x + y

        my_function(1, 2)
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "w") as f:
                        f.write(f"{func.__name__} ok")

                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {type(e).__name__} ({e}). Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "w") as f:
                        f.write(f"{func.__name__} error: {type(e).__name__} ({e}). Inputs: {args}, {kwargs}")

                raise e

        return inner

    return wrapper
