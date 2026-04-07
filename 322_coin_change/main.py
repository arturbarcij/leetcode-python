from solution import Solution

s = Solution()
 
tests = [[[1,2,5], 11, 3],
         [[1,2,5], 3, -1],
         [[1], 0, 0]
        ]
    
for coins, amount, expected in tests:
    got = s.coinChange(coins, amount)
    status = "PASS" if got == expected else "FAIL"
    print(f"status:{status} | coins:{coins} | amount:{amount} | expected:{expected}")
