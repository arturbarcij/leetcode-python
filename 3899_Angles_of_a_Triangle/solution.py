from typing import List
from math import sqrt, degrees, acos
class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        a, b, c = [float(x) for x in sides]
        s = 1/2*(a + b+ c)
        product = (s*(s - a)*(s-b)*(s-c))
        if product > 0:
            area = sqrt(product)
            if area > 0:
                cos_a = (b**2 + c**2 - a**2) / (2*b*c)
                cos_b = (c**2 + a**2 - b**2) / (2*c*a)
                cos_c = (a**2 + b**2 - c**2) / (2*a*b)
                cosines = [cos_a, cos_b, cos_c]
                arccosines = [acos(x) for x in cosines]
                angles = [degrees(x) for x in arccosines]
                angles.sort()
            
            return angles
        else:
            return []
        
            