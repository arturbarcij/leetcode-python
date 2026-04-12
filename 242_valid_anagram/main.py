from solution import Solution

s = Solution()

tests = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("aab", "ab", False),
]

for s1, t, expected in tests:
    got = s.isAnagram(s1, t)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | s={s1!r} t={t!r} | got={got} | expected={expected}")
