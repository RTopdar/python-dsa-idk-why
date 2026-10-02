def powerOfThree(n):
    if n<3 and n !=1:
        return False
    elif n==1:
        return True
    elif(n%3 != 0):
        return False
    else:
        return powerOfThree(n//3)

print(powerOfThree(2))