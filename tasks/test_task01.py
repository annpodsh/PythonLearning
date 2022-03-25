import pytest
import time
import tasks.task01


@pytest.mark.parametrize(
    "value",
    [
        (100, 40000)
    ]
)
def test_cache(value: int):
    first_time = time.time()
    actual_result = tasks.task01.f(*value)
    print(f"\nFirst call: {str(time.time() - first_time)}")
    second_time = time.time()
    expect_result = tasks.task01.f(*value)
    print(f"Second call: {format(str(time.time() - second_time))}")
    assert actual_result is expect_result
