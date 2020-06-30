# Python3

import sys


def pisano(m):
    left, right = 0, 1
    for i in range(0, m * m):
        left, right = right, (left + right) % m
        if left == 0 and right == 1:
            return i + 1


def modulo(n, m):
    pisano_periode = pisano(m)
    n = n % pisano_periode
    if n == 0:
        return 0
    elif n == 1:
        return 1
    left = 0
    right = 1
    for _ in range(n - 1):
        left, right = right, left + right
    return right % m


input = sys.stdin.read()
n, m = map(int, input.split())
print(modulo(n, m))
