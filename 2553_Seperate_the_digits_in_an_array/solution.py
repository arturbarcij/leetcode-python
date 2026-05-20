from main import Solution

s = Solution()

tests = [
    ([13,25,83,77], [1,3,2,5,8,3,7,7]),
    ([7,1,3,9], [7,1,3,9])
    ]

for numbers, expected in tests:
    got = s.separateDigits(numbers)
    status = "PASS" if got == expected else "FAIL"
    print(f" status: {status} | numbers: {numbers} | got: {got}")