from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            elif i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            elif board[i][j] != word[index]:
                return False

            board[i][j] = "#" # mark visited
            result = (dfs(i+1, j, index+1) or
                      dfs(i-1, j, index+1) or
                      dfs(i, j+1, index+1) or
                      dfs(i, j-1, index+1))
            board[i][j] = word[index] # unmark (backtrack)
            return result
        
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False