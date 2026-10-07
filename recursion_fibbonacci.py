def trib(n):
    if n == 0:
        return n
    if n == 2 or n == 1:
        return 1
    return trib(n - 1) + trib(n - 2) + trib(n - 3)


for i in range(20):
    print(trib(i))


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

