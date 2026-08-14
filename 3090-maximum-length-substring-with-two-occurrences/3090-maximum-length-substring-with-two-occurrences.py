class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        lftLst = iter(s)
        ans, left = 0, next(lftLst)
        ctr = defaultdict(int)
        for rght in s:
            ctr[rght]+= 1
            while ctr[rght] == 3:
                ctr[left] -= 1
                left = next(lftLst)
            ans = max(ans,sum(ctr.values()))
        return ans