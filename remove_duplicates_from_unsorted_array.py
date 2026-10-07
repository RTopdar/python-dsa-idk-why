array = [1,2,1,2,3,4,6,4,5,6,5,3,2,3,1,5,4,6,3,1,2]

i = 0

# while i<len(array)-1:
#     if array.count(array[i]) !=1:
#         for j in range( len(array)-1, i , -1):
#             if array[i]==array[j]:
#                 array.pop(j)
#     i +=1
for i in array:
    while array.count(i) > 1:
        array.pop(array.index(i,2))
array.sort()
print(array)