def fib(n):
    if n == 0:
        return n
    if n == 2 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2) + fib(n - 3)


for i in range(20):
    print(fib(i))
