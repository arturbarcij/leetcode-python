from solution import Solution

s = Solution()

tests = [([1,2,3,3], [3,4,5,6], [50,10,40,70], 120),
        ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150)
        ]
for startTime, endTime, profit, expected in tests:
    got = s.jobScheduling(startTime, endTime, profit)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | start_time:{startTime} | end_time:{endTime} | profit:{profit} | expected:{expected}")
