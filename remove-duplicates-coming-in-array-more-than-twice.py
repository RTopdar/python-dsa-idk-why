array = [1,2,1,2,3,4,6,4,5,6,5,3,2,3,1,5,4,3,1,2,3,6,4,3,1,2,3,4,2,2,1]

for i in array:
    while array.count(i)>2:
        array.pop(array.index(i,3))

print(f"Final result is {array}")
for i in set(array):
    print(f"{i} appeared {array.count(i)} times")