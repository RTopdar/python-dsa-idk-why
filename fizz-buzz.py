list = []
for i in range(1, 101):
    list.append(i)
for i in list:
    print("fizz") if i % 3 == 0 else print("buzz") if i % 5 == 0 else print(i)
