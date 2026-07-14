from solution import Solution

s = Solution()


tests = [
    (100, 300, [123,234]),
    (1000,13000,[1234,2345,3456,4567,5678,6789,12345])
]

for low, high, expected in tests:
    got = s.sequentialDigits(low, high)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | got:{got} | expected:{expected}")