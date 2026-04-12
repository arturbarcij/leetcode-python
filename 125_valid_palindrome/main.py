from solution import Solution

s = Solution()

tests = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
]

for string, expected in tests:
    got = s.isPalindrome(string)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | s={string!r} | got={got} | expected={expected}")
