from solution import Solution

s = Solution()

tests = [
    (["A","A","A","B","B","B"], 2, 8),
    (["A","C","A","B","D","B"], 1, 6),
    (["A","A","A","B","B","B"], 0, 6),
]

for tasks, n, expected in tests:
    got = s.leastInterval(tasks, n)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | tasks={tasks} n={n} | got={got} | expected={expected}")
