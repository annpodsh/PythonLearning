import hw3


def test_combinations():
    assert hw3.combinations([1, 2], [3, 4]) == [
        [1, 3],
        [2, 3],
        [1, 4],
        [2, 4],
    ]
