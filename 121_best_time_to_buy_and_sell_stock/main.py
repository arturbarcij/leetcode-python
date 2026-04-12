from solution import Solution

s = Solution()

tests = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1],   0),
    ([1,2],         1),
]

for prices, expected in tests:
    got = s.maxProfit(prices)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | prices={prices} | got={got} | expected={expected}")
