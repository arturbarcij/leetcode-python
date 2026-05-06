from solution import Solution

s = Solution()

tests = [
    ("abcd", "cdab", True),
    ("abcd", "dacb", False)
]

for str1, str2, expected in tests:
    got = s.canBeEqual(str1, str2)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | s1:{str1} | s2:{str2} | got:{got}")