import homework4.tasks.task01
import pytest

"""
Test for finding in different data and in the same
"""


@pytest.mark.parametrize(
    ["keywords", "data", "expected_result"],
    [
        ({"example_key1": "res_one"},
         [{"example_key1": "res_one"}, {"wrong_key2": "res2"}],
         [{"example_key1": "res_one"}]),

        ({"same_key1": "same_res1"},
         [{"same_key1": "same_res1"}, {"same_key1": "same_res1"}],
         [{"same_key1": "same_res1"}, {"same_key1": "same_res1"}])
    ]
)
def test_make_filter(keywords, data, expected_result):
    assert homework4.tasks.task01.make_filter(**keywords).apply(data) == expected_result
