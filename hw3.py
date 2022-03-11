"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    result = []
    for item in args[0]:
        result.append([item])
    for i in range(1, len(args), 1):
        temp_result = result
        result = []
        for item in args[i]:
            for item_list in temp_result:
                item_list_copy = item_list.copy()
                item_list_copy.append(item)
                result.append(item_list_copy)
    return result


print(combinations([1, 2], [3, 4], [5, 6]))
