from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_count = max(count.values())
        task_share_count = sum(1 for v in count.values() if v == max_count)

        min_time = (max_count - 1) * (n + 1) + task_share_count
        return max(min_time, len(tasks))
