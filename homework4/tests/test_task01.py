import homework4.tasks.task01
import pytest

"""
Test for finding in different data and in the same
"""


@pytest.mark.parametrize(
    ["keywords", "data", "expected_result"],
    [
        ({"key1": "res1"}, [{"key1": "res1"}, {"key2": "res2"}], [{"key1": "res1"}]),
        ({"key1": "res1"}, [{"key1": "res1"}, {"key1": "res1"}], [{"key1": "res1"}, {"key1": "res1"}])
    ]
)
def test_make_filter(keywords, data, expected_result):
    assert homework4.tasks.task01.make_filter(**keywords).apply(data) == expected_result
