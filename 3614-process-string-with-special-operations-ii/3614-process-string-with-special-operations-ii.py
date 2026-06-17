class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0 
        for ch in s:
            if ch == "*":
                l = max(0,l-1)
            elif ch == "#":
                l *= 2
            elif ch == "%":
                continue
            else:
                l += 1
        if k>=l:
            return '.'
        for ch in s[::-1]:
            if ch=="*":
                l += 1
            elif ch == "#":
                l = l//2
                if k>=l:
                    k-=l
            elif ch == "%":
                k = l-k-1
            else:
                if k==l-1:
                    return ch
                l-=1