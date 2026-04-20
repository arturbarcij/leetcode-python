from typing import List
from bisect import bisect_right
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        distance = 1
        max_distance = 0
        arr2 = [-x for x in nums2] # switch from descending to ascending order
        
        for i in range(n):
            pos = bisect_right(arr2, -nums1[i]) # negate nums1[i]
            j = pos - 1
            if j >= i: # valid pairs
                max_distance = max(j - i, max_distance)

        return max_distance