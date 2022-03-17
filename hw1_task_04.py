"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import random
import time
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    ab = dict()
    for i in a:
        for j in b:
            ab.update({i + j: ab.get(i * j, 0) + 1})
    cd = dict()
    for k in c:
        for l in d:
            cd.update({k + l: ab.get(k * l, 0) + 1})
    count = 0
    for itemAB in ab:
        count += ab.get(itemAB) * cd.get(-itemAB, 0)
    return count


N = 1000
range_of_values = 1000
A = []
B = []
C = []
D = []
for i in range(0, N):
    A.append(random.randint(-range_of_values, range_of_values))
    B.append(random.randint(-range_of_values, range_of_values))
    C.append(random.randint(-range_of_values, range_of_values))
    D.append(random.randint(-range_of_values, range_of_values))
print(check_sum_of_four(A, B, C, D))
