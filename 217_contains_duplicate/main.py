from solution import Solution

s = Solution()
tests = [
    ([1, 2, 3, 1], True),
    ([1, 2, 3, 4], False),
    ([1],          False),
]

for nums, expected in tests:
    got = s.containsDuplicate(nums)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | input={nums} | got={got} | expected={expected}")