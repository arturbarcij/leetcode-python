from solution import Solution

s = Solution()

tests = [
    ([1, 2, 3, 4, 5], 5, 3, 1),
    ([1], 1, 0, 0),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0, 0),
    ([1, 2, 3, 4, 5], 1, 4, 4),
    ([5, 3, 6], 5, 2, 2),
]

for nums, target, start, expected in tests:
    got = s.getMinDistance(nums, target, start)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} target={target} start={start} | got={got} | expected={expected}")
