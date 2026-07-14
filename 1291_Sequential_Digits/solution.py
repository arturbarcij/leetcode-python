from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        results = []
        for length in range(2, 10):
            for start in range(0, len(s) - length + 1):
                chunk = s[start:start + length]
                num = int(chunk)
                if low <= num <= high:
                    results.append(num)
        
        return results
            