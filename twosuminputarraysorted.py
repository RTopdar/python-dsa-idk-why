def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left<right:
        sum1 = numbers[left]+numbers[right]
        if sum1 == target:
            return [left, right]
        elif sum1 > target:
            right-=1
        else:
            left +=1
print(twoSum([2,3,4],6))