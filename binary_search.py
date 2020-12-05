def binary(a, low, high, x):
    #print(a)
    #print(low)
    #print(high)
    if high < low:
        return -1

    mid = low + (high - low) // 2

    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return binary(a, low, mid -1, x)
    else:
        return binary(a, mid + 1, high, x)

#5 1 5 8 12 13
#5 8 1 23 1 11
data = list(map(int, input().split()))
search = list(map(int, input().split()))
n = data[0]
a = data[1:]
x = search[1:]
for i in range(len(x)):
    print(binary(a, 0, n - 1, x[i]), end=' ')