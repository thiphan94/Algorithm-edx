# Uses python3
import sys


def optimal_j(W, w):
    # write your code here
    stock = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            stock[i][j] = stock[i - 1][j]
            if w[i - 1] <= j:
                change = stock[i - 1][j - w[i - 1]] + w[i - 1]
                if change > stock[i][j]:
                    stock[i][j] = change
    return stock[n][W]


if __name__ == "__main__":
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_j(W, w))
