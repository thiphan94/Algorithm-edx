# Uses python3
def edit_distance(s, t):
    m = len(s)
    n = len(t)
    stock = [[[None] for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                stock[i][j] = j
            elif j == 0:
                stock[i][j] = i
            elif s[i - 1] == t[j - 1]:
                stock[i][j] = stock[i - 1][j - 1]
            else:
                stock[i][j] = (
                    min(stock[i][j - 1], stock[i - 1][j], stock[i - 1][j - 1]) + 1
                )

    return stock[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
