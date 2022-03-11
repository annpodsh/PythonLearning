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
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    count = 0
    start_time = time.time()
    """
    for aa in a:
        for bb in b:
            b_summary = aa + bb
            if b_summary + c[len(c) - 1] + d[len(d) - 1] < 0 or b_summary + c[0] + d[0] > 0:
                continue
            for cc in c:
                c_summary = b_summary + cc
                if c_summary + d[len(d) - 1] < 0 or c_summary + d[0] > 0:
                    continue
                left = 0
                right = len(d) - 1
                index = -1
                result = False
                while right > left:
                    index = int((left + right) / 2)
                    summary = c_summary + d[index]
                    if summary > 0:
                        right = index - 1
                    elif summary < 0:
                        left = index + 1
                    else:
                        count += 1
                        result = True
                        break
                if result:
                    index_forward = index + 1
                    index -= 1
                    while c_summary + d[index_forward] == 0:
                        count += 1
                        index_forward += 1
                    while c_summary + d[index] == 0:
                        count += 1
                        index -= 1
        print(time.time() - start_time)
    """
    ab = []
    for aa in a:
        for bb in b:
            ab.append(aa + bb)
    cd=[]
    for cc in c:
        for dd in d:
            cd.append(cc+dd)
    print("sort")
    cd.sort()
    print("sort done")
    for aabb in ab:
        left = 0
        right = len(cd) - 1
        index = -1
        result = False
        while right > left:
            index = int((left + right) / 2)
            summary = aabb + cd[index]
            if summary > 0:
                right = index - 1
            elif summary < 0:
                left = index + 1
            else:
                count += 1
                result = True
                break
        if result:
            index_forward = index + 1
            index -= 1
            while aabb + cd[index_forward] == 0:
                count += 1
                index_forward += 1
            while aabb + cd[index] == 0:
                count += 1
                index -= 1
    return count


N = 1000
range_of_values = 20000
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
