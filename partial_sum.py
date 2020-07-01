# Python3

import sys


def fibo(n):
    n = (n + 2) % 60
    left = 0
    right = 1
    for _ in range(n - 1):
        left, right = right % 10, (left + right) % 10
    return right


input = sys.stdin.read()
a, b = map(int, input.split())
print((fibo(b) - fibo(a - 1)) % 10)
