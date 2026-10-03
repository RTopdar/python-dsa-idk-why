arr = [2,-9,3,8,7,-6,1,4,5]
max_sum = float('-inf')
max_subarray = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
        subarray = arr[i:j]
        current_sum = sum(subarray)
        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray = subarray

print(f"Max subarray: {max_subarray}")
print(f"Max sum: {max_sum}")