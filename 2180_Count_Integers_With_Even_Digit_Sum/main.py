from solution import Solution

s = Solution()

# Each case: (input num, expected count)
tests = [
    (4, 2),      # example 1: 2, 4
    (30, 14),    # example 2
    (1, 0),      # smallest input, digit sum of 1 is odd
    (2, 1),      # only 2 qualifies
    (11, 5),     # 2, 4, 6, 8, 11
]

for num, expected in tests:
    got = s.countEven(num)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | input={num} | got={got} | expected={expected}")
