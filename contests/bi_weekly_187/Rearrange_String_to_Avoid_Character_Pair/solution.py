class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # Every y must come before every x, so put all the y's up front.
        # Everything else (including the x's) follows in any order.
        ys = y * s.count(y)
        rest = ''.join(c for c in s if c != y)
        return ys + rest
