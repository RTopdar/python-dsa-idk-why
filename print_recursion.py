def printNumbers(n):
    if n == 0: return
    print(n)
    printNumbers(n-1)
def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
print(factorial(9))
