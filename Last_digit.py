# Python3


def fibo(n):
    if n <= 1:
        return n
    left = 0
    right = 1
    for _ in range(n - 1):
        left, right = right % 10, (left + right) % 10
    return right


n = int(input())
print(fibo(n))
