class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        edges = []
        count = 0
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    count += 1
            
            edges.append(count)
            count = 0
        
        return edges