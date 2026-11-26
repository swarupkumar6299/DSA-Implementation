class Solution:
    def canAliceWin(self, n: int) -> bool:
        k = 10
        alince = False
        while n>= k:
            n-=k
            k -= 1
            alince = not alince
        return alince
        