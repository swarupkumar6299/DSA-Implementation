import math

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        r = radius
        cx = xCenter
        cy = yCenter

        def distance(x1,y1,x2,y2):
            return math.sqrt((x1-x2)**2 + (y1-y2)**2)

        # case 1: rectangle check
        if cx >= x1 - r and cx <= x2 + r:
            if cy >= y1 and cy <= y2:
                return True
        if cy >= y1 - r and cy <= y2 + r:
            if cx >= x1 and cx <= x2:
                return True

        # case 2: corner check
        if distance(x1,y1,cx,cy) < r:
            return True
        if distance(x1,y2,cx,cy) < r:
            return True
        if distance(x2,y1,cx,cy) < r:
            return True
        if distance(x2,y2,cx,cy) < r:
            return True

        return False