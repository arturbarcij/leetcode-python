from solution import Solution

s = Solution()

tests = [
    (25, 27),
    (10, 9),
    (7, 0),
]

for n, expected in tests:
    got = s.mirrorDistance(n)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | n={n} | got={got} | expected={expected}")
