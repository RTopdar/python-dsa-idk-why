arr = [3,2,4]
target = 6

sum_hash = {}

for index, val in enumerate(arr):
    complement = target - val
    if complement in sum_hash:
        print([sum_hash[complement],index])
    sum_hash[val] = index