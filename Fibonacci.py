# Python3


def fibo(n):
    if n <= 1:
        return n
    left = 0
    right = 1
    for _ in range(n - 1):
        left, right = right, left + right
    return right


n = int(input())
print(fibo(n))
