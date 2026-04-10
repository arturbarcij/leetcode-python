from solution import Solution

s = Solution()

tests = [
    ([2,1,5,6,2,3], 10),
    ([2,4],         4),
    ([1],           1),
]

for heights, expected in tests:
    got = s.largestRectangleArea(heights)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | heights={heights} | got={got} | expected={expected}")
