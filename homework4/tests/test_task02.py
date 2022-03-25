import homework4.tasks.task02
import pytest
import os

"""
Check successful cases
"""


# Добавить фикстуры


@pytest.mark.parametrize(
    ["input_value"],
    [
        [1.0], [1.5], [2.0], [2.5], [2.9]
    ]
)
def test_read_magic_number_success(input_value: float):
    path = "test_temp_file"
    with open(path, "w+") as fi:
        fi.write(str(input_value))
    assert homework4.tasks.task02.read_magic_number(path)
    os.remove(path)


"""
Check unsuccessful cases
"""


@pytest.mark.parametrize(
    ["input_value"],
    [
        [0.0], [0.5], [-1], [3], [10]
    ]
)
def test_read_magic_number_failure(input_value: float):
    path = "test_temp_file"
    with open(path, "w+") as fi:
        fi.write(str(input_value))
    assert not homework4.tasks.task02.read_magic_number(path)
    os.remove(path)


"""
Check error cases
"""


@pytest.mark.parametrize(
    ["input_value"],
    [
        ["a"], ["Not_A_Number"]
    ]
)
def test_read_magic_number_error(input_value: str):
    path = "test_temp_file"
    with open(path, "w+") as fi:
        fi.write(str(input_value))
    try:
        homework4.tasks.task02.read_magic_number(path)
        assert False
    except ValueError:
        assert True
    os.remove(path)
