from typing import List
from bisect import bisect_right
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        if nums is None:
            return -1
        
        values = dict()
        index_map = {}
        n = len(nums)
        min_distance = float('inf')
        
        for idx, val in enumerate(nums):        # idx = index, val = number at that index
            if val not in index_map:            # if we haven't seen this number before
                index_map[val] = []             # create an empty list for it
            index_map[val].append(idx)          # add this index to that number's list

        def reverse(m):
            if m == 0:
                return 0
            return int(str(m)[::-1])            # reverse input: int -> str -> rev(str) -> int
        
        for i in range(len(nums)):
            rev_num = reverse(nums[i])
            if rev_num in index_map:
                pos = bisect_right(index_map[rev_num], i)     # strictly idx > i thus bisect_right to find closest element
                if pos < len(index_map[rev_num]):    # checks that pos is within bounds
                    j = index_map[rev_num][pos]
                    result = abs(i - j)
                    min_distance = min(min_distance, result)
        return -1 if min_distance == float('inf') else min_distance