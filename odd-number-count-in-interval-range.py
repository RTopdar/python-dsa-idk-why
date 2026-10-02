low = int(input("Enter a low range: "))
high = int(input("Enter a high range: "))

count = sum(1 for i in range(low, high + 1) if i % 2 != 0)

print(count)
