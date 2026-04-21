from functools import lru_cache

def count_divisible_by_3(n):
    s = str(n)

    @lru_cache(None)
    def dp(pos, remainder, tight):
        if pos == len(s):
            return 1 if remainder == 0 else 0
        limit = int(s[pos]) if tight else 9
        total = 0
        for d in range(0, limit + 1):
            new_remainder = (remainder + d) % 3
            new_tight = tight and (d == int(s[pos]))
            total += dp(pos + 1, new_remainder, new_tight)
        return total

    return dp(0, 0, True)

# n=20 → 3,6,9,12,15,18 = 6
print(count_divisible_by_3(20))  # expected: 6
print(count_divisible_by_3(9))   # expected: 3
print(count_divisible_by_3(100)) # expected: 34
