arr = [1,3,4,5,6]

"""
Expected output: [1,4,8,13,19]
"""
res = []
for i in range(len(arr)):
    res.append(sum(arr[:i+1]))

print(res)