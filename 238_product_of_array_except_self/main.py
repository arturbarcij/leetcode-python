from solution import Solution

s = Solution()

tests = [
    ([1, 2, 3, 4], [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ([1, 1], [1, 1]),
]

for nums, expected in tests:
    got = s.productExceptSelf(nums)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} | got={got} | expected={expected}")
