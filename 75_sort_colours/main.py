from solution import Solution

s = Solution()

tests = [([2,0,2,1,1,0], [0,0,1,1,2,2]),
         ([2,0,1], [0,1,2])]

for nums, expected in tests:
    s.sortColors(nums)
    status = "PASS" if nums == expected else "FAIL"
    print(f"{status} | got={nums} | expected={expected}")