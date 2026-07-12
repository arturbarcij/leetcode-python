from solution import Solution

s = Solution()

# Each case: (input arr, expected ranks)
tests = [
    ([40, 10, 20, 30], [4, 1, 2, 3]),   # all distinct
    ([100, 100, 100], [1, 1, 1]),        # all equal -> same rank
    ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),  # duplicates
    ([42], [1]),                         # single element
    ([], []),                            # empty input (guard clause)
    ([-5, 0, -5, 10], [1, 2, 1, 3]),     # negatives + duplicate
]

for arr, expected in tests:
    result = s.arrayRankTransform(arr)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} | input={arr} | got={result} | expected={expected}")
