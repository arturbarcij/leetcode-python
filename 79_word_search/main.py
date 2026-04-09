from solution import Solution

s = Solution()

tests = [
    # Input: board=ABCE/SFCS/ADEE, word="ABCCED" -> Output: True
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True),
    # Input: board=ABCE/SFCS/ADEE, word="SEE" -> Output: True
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True),
    # Input: board=ABCE/SFCS/ADEE, word="ABCB" -> Output: False (can't reuse cell)
    ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False),
    # Input: single cell, word="a" -> Output: True
    ([["a"]], "a", True),
]

for board, word, expected in tests:
    got = s.exist(board, word)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status} | word={word} | got={got} | expected={expected}")
