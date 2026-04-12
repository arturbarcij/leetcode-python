from solution import Solution

s = Solution()

tests = [
    ([[1,3],[-2,2]], 1, [[-2,2]]),
    ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),
]

for points, k, expected in tests:
    got = s.kClosest([p[:] for p in points], k)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")
