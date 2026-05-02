from solution import Solution

s = Solution()


tests = [
    (101, 0, True),
    (232, 2, False),
    (5,1,False)
]


for num, num2, expected in tests:
    got = s.validDigit(num, num2)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | num:{num} | num2:{num2} | expected:{expected} | got:{got}")