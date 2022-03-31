from homework5.tasks.save_original_info import my_decorator
from typing import Callable


def test_my_decorator():
    def example_decorator(func: Callable) -> Callable:
        @my_decorator(original_func=func)
        def wrapper(*args, **kwargs):
            """Wrong example __doc__"""
            return False

        return wrapper

    @example_decorator
    def func_with_correct_name(*args) -> bool:
        """Correct example __doc__"""
        return True

    assert not func_with_correct_name()
    assert func_with_correct_name.__original_func()
    assert func_with_correct_name.__name__ == "func_with_correct_name"
    assert func_with_correct_name.__doc__ == "Correct example __doc__"
