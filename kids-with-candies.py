candies = [6, 8, 2, 4, 9, 1]

extra_candies = 3

result = []

for i in candies:
    result.append(1) if i + extra_candies > max(candies) else result.append(0)

print(result)
