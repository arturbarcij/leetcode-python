from solution import Solution

s = Solution()

tests = [
    ([[1,1,1],[1,1,0],[1,0,1]], 0, 0, 2, [[2,2,2],[2,2,0],[2,0,1]]),
    ([[0,0,0],[0,0,0]], 0, 0, 0, [[0,0,0],[0,0,0]]),
    ([[0,0,0],[0,1,1]], 1, 1, 1, [[0,0,0],[0,1,1]]),
]

for image, sr, sc, color, expected in tests:
    got = s.floodFill(image, sr, sc, color)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")
