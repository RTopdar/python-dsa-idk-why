def isUnique(s:str)->bool:
    return len(set(s)) == len(s)
def longestUniqueSubstring(s:str)->str:
    longest_str=""
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            substring = s[i:j]
            if isUnique(substring)==True and len(substring)>len(longest_str):
                longest_str = substring
    return longest_str

print(longestUniqueSubstring("abcbacdac"))