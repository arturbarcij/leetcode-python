from solution import Solution

s = Solution()


tests = [
    ([1,3,2,1],1),
    ([2,4,5,2],0),
    ([1,2,4,3],-1)
]


for arr, expected in tests:
    got = s.compareBitonicSums(arr)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | arr:{arr} | expected:{expected} | got:{got}")