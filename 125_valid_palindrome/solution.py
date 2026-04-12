import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return ans == ans[::-1]
