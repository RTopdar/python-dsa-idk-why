from collections import Counter
def firstUniqueChar(str):
    # charset = set()
    # lowest_index=-1
    # for index, char in reversed(list(enumerate(str))):
    #     if char not in charset:
    #         charset.add(char)
    #         lowest_index = index
    count = Counter(str)
    print(count)
    for index, char in enumerate(str):
        if count[char]==1:
            return index
    return -1
    # return lowest_index

print(firstUniqueChar("ooo"))

