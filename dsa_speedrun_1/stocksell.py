def stocksell(arr):
    min_val = arr[0]
    top_profit = 0
    for i in arr:
        min_val = min(min_val, i)
        top_profit = max(top_profit, i-min_val)
    return top_profit


print(stocksell([7,1,5,3,6,4]))
print(stocksell([7,6,4,3,1]))
print(stocksell([2,4,1]))
