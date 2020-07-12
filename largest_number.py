# Uses python3

import sys


def isgreaterorequal(a, b):
    a, b = str(a), str(b)
    if int(a + b) >= int(b + a):
        return True
    else:
        return False


def largest_number(a):
    res = ""
    while a != []:
        max = 0
        for i in a:
            if isgreaterorequal(i, max):
                max = i
        res += max
        a.remove(max)
    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
