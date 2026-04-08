from typing import List
from bisect import bisect_right
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        end_times = [job[1] for job in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            start, end, prof = jobs[i - 1]
            idx = bisect_right(end_times, start) - 1
            dp[i] = max(dp[i - 1], dp[idx + 1] + prof)
            
        return dp[n]
        