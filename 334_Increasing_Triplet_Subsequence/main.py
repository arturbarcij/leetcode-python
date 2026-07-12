from solution import Solution

s = Solution()

tests = [
    ([1,2,3,4,5], True),
    ([5,4,3,2,1], False),
    ([2,1,5,0,4,6], True),
    ([20,100,10,12,5,13], True),
    ([2,2,2,2], False),
    ([1,2], False),
    ([1], False)    
]

for arr, expected in tests:
    got = s.increasingTriplet(arr)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | got={got} | expected={expected}")