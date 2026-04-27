from collections import defaultdict
from typing import List
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        min_dist = float('inf')
        frequency = defaultdict(list)
        
        for j in range(n):
            frequency[nums[j]].append(j)
        
        for key, occ_list in frequency.items():
            if len(occ_list) >= 3:
                for i in range(len(occ_list) - 2):
                    dist = 2*(occ_list[i+2] - occ_list[i])
                    min_dist = min(min_dist, dist)
        
        if min_dist == float('inf'):
            return -1
        else:
            return min_dist               