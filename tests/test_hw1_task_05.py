import hw1_task_05


def test_find_maximal_subarray_sum():
    assert hw1_task_05.find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16
    assert hw1_task_05.find_maximal_subarray_sum([1, 2, 3, 4, 5, 6], 4) == 18
