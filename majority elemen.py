n = int(input())
a = list(map(int, input().split()))


def majority_element(a, n):
    mid = (n - 1) // 2
    a = sorted(a)
    count = a.count(a[mid])
    if count > n / 2:
        return 1
    else:
        return 0


print(majority_element(a, n))
