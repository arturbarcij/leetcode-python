from solution import Solution

s = Solution()

tests = [([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
         ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]])
        ]

for intervals, newInterval, expected in tests:
    got = s.insert(intervals, newInterval)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | input ={intervals} | got={got} | expected={expected}")
    