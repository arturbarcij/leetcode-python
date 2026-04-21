from solution import Solution

s = Solution()

tests = [
    (8, 10, "DDDRRR", 2),
    (123456789, 123456790, "DDRRDR", 1),
    (1288561398769758, 1288561398769758, "RRRDDD", 0),
]

for l, r, directions, expected in tests:
    got = s.countGoodIntegersOnPath(l, r, directions)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | l={l} r={r} directions={directions} | got={got} | expected={expected}")
