class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        evens_s1 = sorted([s1[0], s1[2]])
        evens_s2 = sorted([s2[0], s2[2]])
        
        odds_s1 = sorted([s1[1], s1[3]])
        odds_s2 = sorted([s2[1], s2[3]])
        
        return evens_s1 == evens_s2 and odds_s1 == odds_s2