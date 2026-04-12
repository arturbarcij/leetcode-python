from solution import Solution

s = Solution()

tests = [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5),
    ("hit", "cog", ["hot","dot","dog","lot","log"], 0),
    ("a", "c", ["a","b","c"], 2),
]

for begin, end, wordList, expected in tests:
    got = s.ladderLength(begin, end, wordList[:])
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | {begin!r}->{end!r} | got={got} | expected={expected}")
