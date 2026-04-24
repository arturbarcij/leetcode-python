from solution import Solution

s = Solution()

tests = [
    ("  the sky is blue  ", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
]

for input, expected in tests:
    got = s.reverseWords(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{repr(input)} | expected:{repr(expected)} | got:{repr(got)}")
