def get_optimal_value(n, capacity, weights):
    value = 0.
    weights.sort(key = lambda x: x[0] / x[1], reverse=True)
    for ind in range(0, len(weights), 1):
        value += (weights[ind][0] / weights[ind][1]) * min(weights[ind][1], capacity)
        capacity -= min(capacity, weights[ind][1])
        if capacity <= 0:
            break

    return value


n, W = map(int, input().split())
w = []
for _ in range(n):
    w = (list(map(int, input().split())))
print("{:.10f}".format(get_optimal_value(n, W, w)))
