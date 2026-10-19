def twoSum(nums: list[int], target: int) -> list[int]:
        flag = False
        array = []
        for i in range(len(nums)-1):
            
            for j in range(i+1, len(nums)):
                print(f"i: {i} /t j: {j}")
                if nums[i]+nums[j] == target:
                    print(f"Target found at {i},{j}")
                    array = [i,j]
                    flag = True
                    break
            if flag == True:
                break
        return array
def twoSumWithHash(nums: list[int], target: int):
     hashStore = {}
     for key, value in enumerate(nums):
          complement = target - value
          if complement in hashStore:
               return {
                    "indices": [hashStore[complement],key],
                    "values": [complement, value]
               }
          hashStore[value] = key
     return []
print(twoSumWithHash([3,2,4],6))