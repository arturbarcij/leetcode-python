from functools import lru_cache

class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        # compute the 7 path indices in the 16-digit string
        path = set()
        row, col = 0, 0
        path.add(row * 4 + col)
        for ch in directions:
            if ch == 'D': row += 1
            else: col += 1
            path.add(row * 4 + col)

        def count(n):
            s = str(n).zfill(16)

            @lru_cache(None)
            def dp(pos, last, tight):
                if pos == 16:
                    return 1  # all digits placed, condition never violated

                limit = int(s[pos]) if tight else 9
                total = 0
                for d in range(0, limit + 1):
                    if pos in path:
                        if d < last:
                            continue      # violates non-decreasing
                        new_last = d
                    else:
                        new_last = last   # non-path position, last unchanged

                    new_tight = tight and (d == int(s[pos]))
                    total += dp(pos + 1, new_last, new_tight)
                return total

            return dp(0, -1, True)

        return count(r) - count(l - 1)
