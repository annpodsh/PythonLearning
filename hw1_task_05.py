"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
import random
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    iterator = 1
    subarray = nums[0:k]
    summary = sum(subarray)
    while iterator <= len(nums) - k:
        subarray = nums[iterator:iterator + k]
        temp_summary = sum(subarray)
        if summary < temp_summary:
            summary = temp_summary
        iterator += 1
    print(nums)
    return summary


NUMS = []
o = 8
range1 = 20
for i in range(0, o):
    NUMS.append(random.randint(-range1, range1))
print(find_maximal_subarray_sum(NUMS, 3))
