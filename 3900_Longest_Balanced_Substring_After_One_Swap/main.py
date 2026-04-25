from solution import Solution

s = Solution()

tests = [
    ("100001", 4),
    ("111", 0),
    ()
]


for input, expected in tests:
    got = s.longestBalanced(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected} | got:{got}")