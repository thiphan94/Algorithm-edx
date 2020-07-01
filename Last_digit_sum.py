# Python3

import sys


def fibo_sum(n):
    left = 0
    right = 1
    sum = 1
    if n == 0:
        return left
    elif n == 1:
        return right
    for _ in range(n - 1):
        left, right = right, left + right
        sum += right
    return sum


n = int(input())
print(fibo_sum(n) % 10)
