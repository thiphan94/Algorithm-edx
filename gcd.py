# Python3

import sys

input = sys.stdin.read()
a, b = map(int, input.split())


def cal_gcd(a, b):
    if a >= b:
        dividend = a
        divisor = b
    else:
        dividend = b
        divisor = a
    rest = 0
    while divisor != 0:
        rest = dividend % divisor
        dividend = divisor
        divisor = rest
    return dividend


print(cal_gcd(a, b))
