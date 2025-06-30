class Solution:
    def findLHS(self, nums: List[int]) -> int:
        f = collections.Counter(nums)
        best = 0
        for x in f.keys():
            if f[x]>0 and f[x+1]>0:
                best = max(best,f[x]+f[x+1])
        return best
        