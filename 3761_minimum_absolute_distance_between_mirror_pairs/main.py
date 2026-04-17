from solution import Solution

s = Solution()

tests = [
    ([12, 21, 45, 54], 1),
    ([11, 22, 33], 2),
    ([1, 2, 3], -1),
]

for nums, expected in tests:
    got = s.minAbsDistance(nums)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} | got={got} | expected={expected}")
