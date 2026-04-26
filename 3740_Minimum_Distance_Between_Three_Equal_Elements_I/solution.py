from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        min_distance = float('inf')
        
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):            
                    if nums[i] == nums[j] == nums[k]:
                        distance = abs(i - j) + abs(j - k) + abs(k - i)
                        min_distance = min(min_distance, distance)
        
        
        if min_distance == float('inf'):
            return -1
        else:
            return int(min_distance)