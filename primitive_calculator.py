# Uses python3
import sys


def optimal_sequence(n):
    result = [0 for i in range(0, n + 1)]
    for i in range(2, n + 1):
        min1 = result[i - 1]
        min2 = sys.maxsize
        min3 = sys.maxsize
        if i % 2 == 0:
            min2 = result[int(i / 2)]
        if i % 3 == 0:
            min3 = result[int(i / 3)]
        minOp = min(min1, min2, min3)

        result[i] = minOp + 1

    return result


input = sys.stdin.read()
n = int(input)
sequence = optimal_sequence(n)
print(sequence[n])
for i in range(2, n + 1):
    print(sequence[i], end=" ")
