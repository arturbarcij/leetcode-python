from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # pattern: variable-size sliding window
        t_count = Counter(t) # frequency map of t
        window_count = {} # frequency map of current window
        have = 0
        need = len(t_count)
        left = 0
        result = ""
        result_len = float('inf')
        
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                have += 1
            
            
            while have == need:
                # update best result if this window is smaller
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right + 1]
                
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                left += 1
            
        return result