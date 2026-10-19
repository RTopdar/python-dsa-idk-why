def isUnique(s:str)->bool:
    return len(set(s)) == len(s)
def countGoodSubstrings(s:str):
    result=[]
    for i in range(len(s)-2):
        substring = s[i:i+3]
        if isUnique(substring)==True:
            result.append(substring)
    return result

def run_tests():
    unique_cases = [
        ("abc", True),
        ("aba", False),
        ("", True),
        ("a", True),
        ("aa", False),
        ("a a", False),
        ("aAb", True),
        ("aAa", False),
    ]
    good_cases = [
        ("abcabc", ["abc", "bca", "cab", "abc"]),
        ("aaaa", []),
        ("abac", ["bac"]),
        ("abcd", ["abc", "bcd"]),
        ("ab", []),
        ("", []),
        ("a", []),
        ("abc", ["abc"]),
        ("aaa", []),
        ("aab", []),
        ("abb", []),
        ("aba", []),
        ("aAb", ["aAb"]),
        ("aAa", []),
        ("a b", ["a b"]),
        ("a a", []),
        ("abcdef", ["abc", "bcd", "cde", "def"]),
        ("abcabcabc", ["abc", "bca", "cab", "abc", "bca", "cab", "abc"]),
        ("xyzzaz", ["xyz"]),
        ("aababcabc", ["abc", "bca", "cab", "abc"]),
        ("héllo", ["hél"]),
    ]

    passed = 0
    total = 0
    suites = [
        ("isUnique", isUnique, unique_cases),
        ("countGoodSubstrings", countGoodSubstrings, good_cases),
    ]
    for label, func, cases in suites:
        print(f"=== {label} ===")
        for s, expected in cases:
            total += 1
            actual = func(s)
            ok = actual == expected
            passed += ok
            print(f"Test {total}: input={s!r}")
            print(f"  expected: {expected!r}")
            print(f"  actual:   {actual!r}")
            print(f"  {'PASS' if ok else 'FAIL'}")
        print()
    print(f"{passed}/{total} tests passed")

if __name__ == "__main__":
    run_tests()
