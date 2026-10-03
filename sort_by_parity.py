array = [2,9,3,8,7,6,1,4,5]

n = len(array)
left =0
right = n -1

while left<right:
    while right>left and array[right]%2!=0:
        right-=1
    while right>left and array[left]%2==0:
        left+=1
    if left<right:
        array[left],array[right]=array[right], array[left]


            

print(array)




 