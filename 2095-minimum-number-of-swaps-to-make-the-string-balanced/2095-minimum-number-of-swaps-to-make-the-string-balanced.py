class Solution:
    def minSwaps(self, s: str) -> int:
        u = 0
        for c in s:
            u += 1 if c == '[' else -1 if u > 0 else 0
        return (u+1)//2
        