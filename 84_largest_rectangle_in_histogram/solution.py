from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            while stack and heights[stack[-1][0]] >= heights[i]:
                idx, s = stack.pop()
                height = heights[idx]
                width = i - s
                max_area = max(max_area, height * width)
                start = s
            stack.append((i, start))
        
        for i, start in stack:
            height = heights[i]
            width = len(heights) - start
            max_area = max(max_area, height * width)
        
        return max_area