from solution import Solution

s = Solution()

tests = [
    ([3,4,5],[36.86990,53.13010,90.00000]),
    ([2,4,2],[])
]

for input, expected in tests:
    got = s.internalAngles(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected} | got:{got}")