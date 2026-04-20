class Solution:
    def mirrorDistance(self, n: int) -> int:
        result = 0
        
        def reverse(n):
            if n == 0:
                return 0
            
            mirror = 0
            
            mirror = str(n)
            mirror = mirror[::-1]
            return int(mirror)
        
        return abs(n - reverse(n))
        