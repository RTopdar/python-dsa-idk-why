def is_anagram(str1: str, str2: str):
    return (sorted((str1.lower()))==sorted((str2.lower())))

def anagram_grouper(words: list[str]):
    hash_store= {}
    for word in words:
        key = "".join(sorted(word.lower()))
        hash_store.setdefault(key,[]).append(word)
    return list(hash_store.values())

print(anagram_grouper(["anagram","nagaram","rat", "car", "acr"]))