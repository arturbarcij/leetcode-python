from solution import Solution

s = Solution()

tests = [
    ([12, 21, 45, 33, 54], 1),
    ([120, 21], 1),
    ([21, 120], -1),
]

for nums, expected in tests:
    got = s.minMirrorPairDistance(nums)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} | got={got} | expected={expected}")
