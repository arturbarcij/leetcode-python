from solution import Solution

s = Solution()

tests = [([55,30,5,4,2],[100,20,10,10,5], 2),
         ([2,2,2], [10,10,1], 1),
         ([30,29,19,5], [25,25,25,25,25], 2)
        ]


for arr1, arr2, expected in tests:
    got = s.maxDistance(arr1, arr2)
    status = "PASS" if got == expected else "FAIL"
    print(f"nums1:{arr1} | nums2:{arr2} | got:{got} | status:{status}")