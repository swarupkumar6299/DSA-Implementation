class Solution:
    def isHappy(self, n: int) -> bool:
        seem = set()
        if n==1:
            return True
        while n not in seem:
            seem.add(n)
            n = sum([int(d)**2 for d in str(n)])
            if n==1:
                return True
        return False
        