from solution import Solution

s = Solution()

tests = [
    ([1,1,1,6,1,1,1],3),
    ([1,8,3,8,3],4),
    ([0,1],1)
]

for color, expected in tests:
    got = s.maxDistance(color) 
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | color:{color} | expected:{expected} | got:{got}")