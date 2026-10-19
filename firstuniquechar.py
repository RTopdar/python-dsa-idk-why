def firstUniqueChar(str):
    charset = set()
    lowest_index=-1
    for index, char in reversed(list(enumerate(str))):
        if char not in charset:
            charset.add(char)
            lowest_index = index
    return lowest_index

print(firstUniqueChar("ooooo"))

