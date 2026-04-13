from solution import Solution

s = Solution()

tests = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]

for nums, target, expected in tests:
    got = s.twoSum(nums, target)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} target={target} | got={got} | expected={expected}")
