dist = int(input())
m = int(input())
n = int(input())
w = (list(map(int, input().split())))

def car_fuel(dist, m, n, w):
    start = 0
    current = 0
    w = [0] + w + [dist]
    while current < len(w) - 1:
        last_refill = current
        while (current < len(w) - 1) and (w[current + 1] - w[last_refill] <= m):
            current += 1
        if current == last_refill:
            return -1
        if current < len(w) - 1:
            start += 1
        if (m >= dist):
            return 0
        if m < dist - w[len(w) - 1]:
            return -1

    return start

print(car_fuel(dist, m, n, w))