class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,x2,y1,y2=rec1[0],rec1[1],rec1[2],rec1[3]
        c1,c2,d1,d2=rec2[0],rec2[1],rec2[2],rec2[3]

        if c1<y1 and c2<y2 and d1>x1 and d2>x2:
            return True
        return False

        