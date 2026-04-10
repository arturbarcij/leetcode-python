from solution import Solution

s = Solution()

tests = [
    ("1 + 1", 2),
    ("2-1 + 2", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),
    ("1-(     -2)", 3),
    ("- (3 + (4 + 5))", -12),
]

for expr, expected in tests:
    got = s.calculate(expr)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | expr={expr!r} | got={got} | expected={expected}")
