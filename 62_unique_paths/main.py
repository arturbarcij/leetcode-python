from solution import Solution

s = Solution()

tests = [(3, 7, 28),
         (3, 2, 3)]

for m, n, expected in tests:
    got = s.uniquePaths(m, n)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | m={m} n={n} | got={got} | expected={expected}")