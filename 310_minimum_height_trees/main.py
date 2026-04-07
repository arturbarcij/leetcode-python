from solution import Solution

s = Solution()
tests = [
    (4, [[1, 0], [1, 2], [1, 3]],            [1]),
    (6, [[3, 0], [3, 1], [3, 2], [3, 4], [4, 5]], [3, 4]),
    (1, [],                                   [0]),
    (2, [[0, 1]],                             [0, 1]),
]
for n, edges, expected in tests:
    got = sorted(s.findMinHeightTrees(n, edges))
    status = "PASS" if got == sorted(expected) else "FAIL"
    print(f"{status} | n={n} edges={edges} | got={got} | expected={expected}")
