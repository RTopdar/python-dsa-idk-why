def power(n,p):
    if p ==0:
        return 1
    half = power(n,p//2)
    result = half * half
    return result if p%2 ==0 else result * n


print(power(2,8))