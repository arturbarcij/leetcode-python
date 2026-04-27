from solution import Solution

s = Solution()


tests = [
    ([1,2,1,1,3], 6),
    ([1,1,2,3,2,1,2], 8),
    ([1], -1)
]

for input, expected in tests:
    got = s.minimumDistance(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected} | got:{got}")