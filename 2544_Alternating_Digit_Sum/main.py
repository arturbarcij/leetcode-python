class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        ans = 0
        
        for i in enumerate(digits):
            digit = int(i[1])
            if i[0] % 2 == 0:
                ans += digit
            else:
                ans += -digit
        
        return ans
        