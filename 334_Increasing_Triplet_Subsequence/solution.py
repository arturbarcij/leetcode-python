from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                first = n
            elif n <= second: # n > first, so a smaller value exists before n
                second = n
            else:             # n > second > (something before second)
                return True
        
        return False