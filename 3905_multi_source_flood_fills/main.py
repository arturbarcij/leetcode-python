from solution import Solution

s = Solution()

tests = [
    (3, 3, [[0,0,1],[2,2,2]], [[1,1,2],[1,2,2],[2,2,2]]),
    (3, 3, [[0,1,3],[1,1,5]], [[3,3,3],[5,5,5],[5,5,5]]),
    (2, 2, [[1,1,5]], [[5,5],[5,5]]),
]

for n, m, sources, expected in tests:
    got = s.colorGrid(n, m, sources)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | n={n} m={m} sources={sources}")
    if status == "FAIL":
        print(f"  got:      {got}")
        print(f"  expected: {expected}")
