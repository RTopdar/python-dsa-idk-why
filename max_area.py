def max_area(height):
    max_val = max(height)
    second_max=sorted(set(height), reverse=True)[1]
    starting_point = min(height.index(max_val), height.index(second_max))
    end_point = max(height.index(max_val), height.index(second_max))
    width = len(height[
        starting_point:end_point
    ])
    return second_max * width

print(max_area([1,8,6,2,5,4,8,3,7]))