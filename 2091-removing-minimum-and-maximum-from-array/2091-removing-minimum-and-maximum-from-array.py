class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 2
        min_idx = -1
        minVal = inf
        max_idx = n
        maxVal = -inf
        for i, val in enumerate(nums):
            if val<minVal:
                min_idx = i
                minVal = val
            if val>maxVal:
                max_idx = i
                maxVal = val
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        return min(right+1, n-1-left+1, left+1+n-1-right+1)
        