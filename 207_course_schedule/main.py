from solution import Solution

s = Solution()

tests = [
    # Input: n=2, prerequisites=[[1,0]] -> Output: True (take 0 then 1)
    (2, [[1,0]],             True),
    # Input: n=2, prerequisites=[[1,0],[0,1]] -> Output: False (cycle)
    (2, [[1,0],[0,1]],       False),
    # Input: n=1, no prerequisites -> Output: True
    (1, [],                  True),
    # Input: n=4, linear chain -> Output: True
    (4, [[1,0],[2,1],[3,2]], True),
    # Input: n=3, full cycle -> Output: False
    (3, [[0,1],[1,2],[2,0]], False),
]

for n, prereqs, expected in tests:
    got = s.canFinish(n, prereqs)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | n={n} | got={got} | expected={expected}")
