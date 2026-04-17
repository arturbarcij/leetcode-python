from solution import Solution

s = Solution()

tests = [
    ([1, 3, 1, 4, 1, 3], [0, 3, 5], [2, -1, 2]),
    ([1, 2, 3, 1, 2], [0, 1, 2], [2, 2, -1]),
    ([1], [0], [-1]),
]

for nums, queries, expected in tests:
    got = s.solveQueries(nums, queries)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} queries={queries} | got={got} | expected={expected}")
