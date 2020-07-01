# Python3

import sys


def fibo(n):
    n = (n + 2) % 60
    left = 0
    right = 1
    for _ in range(n - 1):
        left, right = right % 10, (left + right) % 10
    if right == 0:
        return 9
    else:
        return right - 1


n = int(input())
print(fibo(n))
