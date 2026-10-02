import math
number = 989893469237864
summation = sum((lambda n: [int(d) for d in str(abs(n))])(number))
product = math.prod((lambda n: [int(d) for d in str(abs(n))])(number))
print(f"Product: {product}")
print(f"Sum: {summation}")
print(f"The difference is {product - summation}")
