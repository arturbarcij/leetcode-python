from solution import Solution

s = Solution()
tests = [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]], [[1,5]]),
    ([[4,7],[1,4]], [[1,7]])
]
for intervals, expected in tests:
    got = s.merge(intervals)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | input={intervals} | got={got} | expected={expected}")