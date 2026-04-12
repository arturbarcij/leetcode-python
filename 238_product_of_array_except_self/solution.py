from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        prefix = 1
        for i in range(n):
            left[i] = prefix
            prefix *= nums[i]
            
        right = [1] * n
        suffix = 1
        for i in range(n-1, -1, -1):
            right[i] = suffix
            suffix *= nums[i]
        
        return [left[i] * right[i] for i in range(n)]