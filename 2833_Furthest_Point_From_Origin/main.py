from solution import Solution

s = Solution()


tests = [
    ("L_RL__R", 3),
    ("_R__LL_", 5),
    ("_______", 7)
]

for input, expected in tests:
    got = s.furthestDistanceFromOrigin(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected} | got:{got}")