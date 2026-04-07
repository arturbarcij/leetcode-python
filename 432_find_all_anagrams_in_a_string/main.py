from solution import Solution

s = Solution()

tests = [
    ("cbaebabacd", "abc", [0, 6]),
    ("abab",       "ab",  [0, 1, 2]),
    ("aa",         "bb",  []),
    ("a",          "a",   [0]),
]

for s_val, p_val, expected in tests:
    got = s.findAnagrams(s_val, p_val)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | s={s_val} p={p_val} | got={got} | expected={expected}")
