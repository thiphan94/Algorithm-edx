# Uses python3
import sys


def get_change(m):
    res = []
    res.append(0)
    res.append(1)
    res.append(2)
    res.append(1)
    res.append(1)
    if m > 4:
        for i in range(5, m + 1):
            value = min(res[i - 4] + 1, min(res[i - 1] + 1, res[i - 3] + 1))
            res.append(value)
    return res[m]


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))
