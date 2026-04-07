from solution import Solution

s = Solution()

tests = [
    ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 1),
    ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 3),
    ([["1"]], 1),
    ([["0"]], 0),
]

for grid, expected in tests:
    got = s.numIslands(grid)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")
