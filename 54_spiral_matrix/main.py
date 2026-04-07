from solution import Solution

s = Solution()
tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],           [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[1, 2, 3, 4]],                                 [1, 2, 3, 4]),
    ([[1], [2], [3]],                                [1, 2, 3]),
]
for matrix, expected in tests:
    got = s.spiralOrder(matrix)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | input={matrix} | got={got} | expected={expected}")
