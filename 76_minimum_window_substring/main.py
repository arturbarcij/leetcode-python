from solution import Solution

s = Solution()

tests = [
    # Input: s = "ADOBECODEBANC", t = "ABC" -> Output: "BANC"
    ("ADOBECODEBANC", "ABC", "BANC"),
    # # Input: s = "a", t = "a" → Output: "a"
    ("a", "a", "a"),
]


for s_val, t_val, expected in tests:
    got = s.minWindow(s_val, t_val)
    status = "PASS" if got == expected else "FAIL"
    print(f"s:{s_val} | t:{t_val} | expected:{expected} | status:{status}")