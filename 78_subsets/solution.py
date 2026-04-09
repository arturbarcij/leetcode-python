from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking problem
        start = 0
        result = []
        
        def dfs(start, current_subset):
            result.append(list(current_subset))
            for i in range (start, len(nums)):
                current_subset.append(nums[i]) # choose
                dfs(i + 1, current_subset)  # explore
                current_subset.pop() # un-choose (backtrack)
                
            
        
        dfs(0, [])
        return result