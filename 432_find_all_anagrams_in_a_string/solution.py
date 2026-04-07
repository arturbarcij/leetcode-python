from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_count = Counter(p)
        window_count = Counter(s[:len(p)])
        left = 0
        right = len(p)

        if window_count == p_count:
            result.append(0)
        
        while right <= len(s) - 1:
            window_count[s[right]] += 1
            
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            
            if window_count == p_count:
                result.append(left + 1)
            
            left += 1
            right += 1
        
        return result