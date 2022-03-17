import hw1_task_04


def test_check_sum_of_four():
    assert hw1_task_04.check_sum_of_four([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == 3 ** 4
    assert hw1_task_04.check_sum_of_four([1, 0, -1], [1, 0, -1], [1, 0, -1], [1, 0, -1]) == 19
