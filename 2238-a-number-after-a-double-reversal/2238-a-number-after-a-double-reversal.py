class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s = str(num)
        s= s[::-1]
        s=int(s)
        s=str(s)
        return int(s[::-1]) == num
        
        