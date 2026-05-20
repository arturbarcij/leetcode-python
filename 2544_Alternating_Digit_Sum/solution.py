from main import Solution

s = Solution()

tests = [
    (521, 4),
    (111, 1),
    (886996, 0)
    ]


for input, expected in tests:
    got = s.alternateDigitSum(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected} | got:{got}")