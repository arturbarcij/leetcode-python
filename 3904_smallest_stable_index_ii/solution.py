from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_max = []
        prefix_max.append(nums[0])
        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]
        
        for i in range(1, n):
            prefix_max.append(max(prefix_max[-1], nums[i]))
        
        for j in range(n-2, -1, -1):
            suffix_min[j] = min(suffix_min[j+1], nums[j])
        
        for i in range(n):
            score = prefix_max[i] - suffix_min[i]
            
            if score <= k:
                return i
        
        return -1