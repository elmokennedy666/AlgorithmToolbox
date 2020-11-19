def get_change(m):
    tens = m // 10
    tens_ = m - tens * 10
    fives = tens_ // 5
    fives_ = tens_ - fives * 5
    ones = fives_ // 1
    m = tens + fives + ones
    return m

m = int(input())
print(get_change(m))