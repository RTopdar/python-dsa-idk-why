array = [1,1,2,2,3,3,4,4,5,5]

i = 0

while i<len(array)-1:
    if array[i]==array[i+1]:
        array.pop(i)
    i+=1

print(array)