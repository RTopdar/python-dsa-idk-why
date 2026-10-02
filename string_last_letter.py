words = ["apple", "dog", "cake", "tree", "house", "cat", "fire", "bird", "orange", "blue", "smile", "run"]

# for word in words:
#     if word[-1] == 'e':
#         print(word)

print([word for word in words if word.endswith('e')])