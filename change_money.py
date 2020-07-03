# Python 3
import sys


def change(a):
    supply = [1, 5, 10]
    n = len(supply)
    change_coins = []
    i = n - 1
    while i >= 0:
        while a >= supply[i]:
            a -= supply[i]
            change_coins.append(supply[i])
        i -= 1
    return len(change_coins)


value = int(sys.stdin.read())
print(change(value))
