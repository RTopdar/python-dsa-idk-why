def common_prefix(strs):
    if not strs:
        return ""

    # for i, char in enumerate(strs[0]):
    #     for word in strs[1:]:
    #         if i >= len(word) or word[i] != char:
    #             return strs[0][:i]
    # return strs[0]
    common = ""
    for i,char in enumerate(strs[0]):
        common += char
        for j in strs[1:]:
            if j.startswith(common) == False:
                return common[:i]
    return common

print(common_prefix(["flower","flow","flight"]))