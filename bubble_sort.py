list = [8,7,5,9,33,4,2,89,47,299,47,1,5,3,9,7,5,4,564,4]

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i]> list[j]:
            list[i], list[j] = list[j],list[i]

print(list)