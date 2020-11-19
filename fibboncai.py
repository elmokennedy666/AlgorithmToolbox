def calc_fib(n):
    if n == 0:
        return [0]
    else:
        fib_list = [0, 1]
        for i in range(2, n+1):
            fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

n = int(input())
print(calc_fib(n)[-1])
