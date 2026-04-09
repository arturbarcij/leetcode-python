from solution import Solution

s = Solution()

tests = [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[],[0]])
]

for input, expected in tests:
    got = sorted(s.subsets(input))
    status = "PASS" if got == sorted(expected) else "FAIL"
    print(f"input:{input} | expected:{expected} | got:{got} | status:{status}")