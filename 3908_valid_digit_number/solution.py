class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        
        for ch in s:
            if str(x) != s[0] and int(ch) == x:
                return True
        return False