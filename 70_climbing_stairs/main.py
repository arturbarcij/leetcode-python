from solution import Solution

s = Solution()

tests = [[2, 2],
         [3, 3]]

for input, expected in tests:
    got = s.climbStairs(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected}")