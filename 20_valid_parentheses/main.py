from solution import Solution

s = Solution()

tests = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(", False),
]

for string, expected in tests:
    got = s.isValid(string)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | s={string} | got={got} | expected={expected}")
