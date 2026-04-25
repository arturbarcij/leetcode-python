#from collections import deque

class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        #queue = deque()
        sum_asc = 0
        sum_desc = 0
        
        def findPeak(nums):
            left = 0
            right = n - 1
            
            while left < right:
                mid = left + (right - left + 1) // 2
                
                #if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                #    return mid
                
                if mid - 1 >= 0 and nums[mid - 1] <= nums[mid]:
                    left = mid
                else:
                    right = mid - 1

                print(f"left:{left}")
                print(f"right:{right}")
            
            return left
                
    
        peak = findPeak(nums)
        print(f"peak:{peak}")
        
        # while left < right:
        #     if nums[left] < nums[left + 1]:
        #         sum_asc += nums[left]
        #     if nums[left] > nums[left + 1]:
        #         sum_desc += nums[left]
        
        
        sum_asc = sum(nums[:peak+1])
        
        sum_desc = sum(nums[peak:n])
        
        print(f"sum_asc:{sum_asc}")
        print(f"sum_desc:{sum_desc}")
        
        if sum_asc > sum_desc:
            return 0
        elif sum_asc < sum_desc:
            return 1
        elif sum_desc == sum_asc:
            return -1