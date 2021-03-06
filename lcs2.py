# Uses python3

import sys


def lcs2(a, b):
    # write your code here
    m = len(a)
    n = len(b)
    stock = [[[None] for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                stock[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                stock[i][j] = stock[i - 1][j - 1] + 1
            else:
                stock[i][j] = max(stock[i][j - 1], stock[i - 1][j])

    return stock[m][n]


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
