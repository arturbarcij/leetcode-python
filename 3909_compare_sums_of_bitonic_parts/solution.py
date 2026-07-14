class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)

        def findPeak(nums):
            left = 0
            right = n - 1

            while left < right:
                mid = left + (right - left + 1) // 2
                if mid - 1 >= 0 and nums[mid - 1] <= nums[mid]:
                    left = mid
                else:
                    right = mid - 1

            return left

        peak = findPeak(nums)

        sum_asc = sum(nums[:peak+1])
        sum_desc = sum(nums[peak:n])

        if sum_asc > sum_desc:
            return 0
        elif sum_asc < sum_desc:
            return 1
        elif sum_desc == sum_asc:
            return -1
