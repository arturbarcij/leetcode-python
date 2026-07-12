from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        sorted_unique_values = sorted(set(arr))
        rank_by_value = {
            value: rank for rank, value in enumerate(sorted_unique_values, start=1)
        }
        return [rank_by_value[value] for value in arr]
