from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            digits = []
            while num > 0:
                digit = num % 10
                digits.append(digit)
                num //= 10

            answer.extend(digits[::-1])

        return answer
