from collections import defaultdict, deque

class Solution:
    def longestBalanced(self, s: str) -> int:
        count_0, count_1 = s.count('0'), s.count('1')
        max_possible = 2 * min(count_0, count_1)

        first_occ = {0: -1}       # first occurrence per prefix sum (for sum=0 case)
        all_occ = defaultdict(deque)  # all occurrences per prefix sum (for sum=±2 case)
        all_occ[0].append(-1)

        running_sum = 0
        max_len = 0

        for i, ch in enumerate(s):
            running_sum += 1 if ch == '1' else -1

            # no swap: window with sum=0 is always valid, first occ gives longest
            if running_sum in first_occ:
                max_len = max(max_len, i - first_occ[running_sum])

            # one swap: window with sum=±2, length must be ≤ max_possible
            for target in (running_sum - 2, running_sum + 2):
                if target in all_occ:
                    dq = all_occ[target]
                    while dq and i - dq[0] > max_possible:
                        dq.popleft()
                    if dq:
                        max_len = max(max_len, i - dq[0])

            if running_sum not in first_occ:
                first_occ[running_sum] = i
            all_occ[running_sum].append(i)

        return max_len
