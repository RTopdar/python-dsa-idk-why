number_array = [5,9,3,7,22,5,9,44,8,9,897,415,365]



for i in number_array:
    print(f"Count of numbers smaller than {i}: {sum(1 for j in number_array if j < i)}")
