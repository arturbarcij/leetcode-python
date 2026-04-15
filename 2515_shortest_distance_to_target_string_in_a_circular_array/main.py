from solution import Solution

s = Solution()

tests = [
    (["hello", "i", "am", "leetcode", "hello"], "hello", 1, 1),
    (["a", "b", "leetcode"], "leetcode", 0, 1),
    (["i", "eat", "leetcode"], "eating", 1, -1),
]

for words, target, startIndex, expected in tests:
    got = s.closestTarget(words, target, startIndex)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | words={words} target={target} startIndex={startIndex} | got={got} | expected={expected}")
