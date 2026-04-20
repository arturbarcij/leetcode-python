from solution import Solution

s = Solution()

tests = [
    ([5,0,1,4],3,3),
    ([3,2,1],1,-1),
    ([-1],0,0)
]


for nums, k, expected in tests:
    got = s.firstStableIndex(nums, k)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | nums={nums} k={k} | got={got} | expected={expected}")
