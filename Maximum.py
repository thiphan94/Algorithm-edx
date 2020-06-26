# Python 3

n = int(input())
l = [int(x) for x in input().split()]
assert len(l) == n
multi = 0

max1 = -1
for i in range(n):
    if max1 == -1 or l[i] > l[max1]:
        max1 = i

max2 = -1
for i in range(n):
    if i != max1 and (max2 == -1 or l[i] > l[max2]):
        max2 = i

print(l[max1] * l[max2])
