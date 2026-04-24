class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        distance = 0
        left = 0
        right = 0
        underscore = 0
        
        for i in range(len(moves)):
            if moves[i] == 'L':
                left += 1
            elif moves[i] == 'R':
                right += 1
            elif moves[i] == '_':
                underscore += 1
                
        distance = abs(left - right) + underscore
        return distance