class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        r = 0
        for x in a:
            count = all(abs(y-x)>d for y in b)
            if count:
                r+=1
        return r
        