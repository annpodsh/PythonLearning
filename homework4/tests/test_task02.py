import homework4.tasks.task02
import pytest
import os

"""
Check successful cases
"""


def setup():
    global path
    path = "test_temp_file"
    fi = open(path, "w+")
    fi.close()


def teardown():
    os.remove(path)


@pytest.mark.parametrize(
    ["input_value"],
    [
        [1.0], [1.5], [2.0], [2.5], [2.9]
    ]
)
def test_read_magic_number_true(input_value: float):
    with open(path, "w") as fi:
        fi.write(str(input_value))
    assert homework4.tasks.task02.read_magic_number(path)


"""
Check unsuccessful cases
"""


@pytest.mark.parametrize(
    ["input_value"],
    [
        [0.0], [0.5], [-1], [3], [10]
    ]
)
def test_read_magic_number_false(input_value: float):
    with open(path, "w") as fi:
        fi.write(str(input_value))
    assert not homework4.tasks.task02.read_magic_number(path)


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
    with open(path, "w") as fi:
        fi.write(str(input_value))
    with pytest.raises(ValueError):
        homework4.tasks.task02.read_magic_number(path)
