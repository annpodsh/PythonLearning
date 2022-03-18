from typing import Any
from typing import List
from typing import Callable


def cache(times: int = 1) -> Callable:
    def decorated_function(func: Callable) -> Callable:
        times_called = times
        result = None

        def cached_func(*args: List[Any]) -> Any:
            nonlocal times_called
            nonlocal result
            if times_called == times:
                result = func(*args)
                times_called = 0
            else:
                times_called += 1
            return result

        return cached_func

    return decorated_function


@cache(times=2)
def f() -> str:
    return input('? ')


print(f())
print(f())
print(f())
print(f())
print(f())
print(f())
