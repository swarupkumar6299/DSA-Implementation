class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        N = len(nums)
        for i in range(N):
            if max(nums[:i+1]) - min(nums[i:])<=k:
                return i
        return -1
        