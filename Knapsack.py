# Python3

import sys
import unittest


def get_optimal_value(capacity, weights, values):
    value = 0.0
    ratio = [float(v) / float(w) for v, w in zip(values, weights)]
    n = len(weights)
    for _ in range(n + 1):
        if capacity == 0:
            return value
            break
        max_ratio = max(ratio)
        index = ratio.index(max_ratio)
        ratio[index] = -1
        add = min(capacity, weights[index])
        value += add * max_ratio
        weights[index] -= add
        capacity -= add
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
