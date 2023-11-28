import sys


def min_Set_size(num, k):
    if num == 0:
        return 0

    for i in range(1, 11):
        if k * i % 10 == num % 10 and i * k <= num:
            return i

    return -1


num = int(input())
k = int(input())
result = min_Set_size(num, k)
print(result)
