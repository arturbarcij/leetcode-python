from solution import Solution

s = Solution()

tests = [
    ([[0,1,1],[1,0,1],[1,1,0]], [2,2,2]),
    ([[0,1,0],[1,0,0],[0,0,0]], [1,1,0]),
    ([[0]], [0])
]


for input, expected in tests:
    got = s.findDegrees(input)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | input:{input} | expected:{expected} | got:{got}")