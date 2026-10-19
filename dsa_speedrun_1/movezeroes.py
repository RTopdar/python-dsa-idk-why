def movezeroes(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        if arr[i]==0 and arr[j]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            i +=1
            j -=1
        else:
            if arr[i]!=0:
                i+=1
            else:
                j-=1
    # write_pos = 0
    # for i in range(len(arr)):
    #     arr[write_pos] = arr[i]
    #     write_pos+=1
    # while write_pos<len(arr):
    #     arr[write_pos]=0
    #     write_pos += 1
    return arr
print(movezeroes([0,1,0,3,12]))