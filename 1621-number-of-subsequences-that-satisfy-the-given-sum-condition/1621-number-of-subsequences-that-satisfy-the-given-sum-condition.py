class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        count = 0
        MOD = 10**9+7
        nums.sort()
        for i in range(N):
            j = bisect_right(nums, target-nums[i]) -1
            if j>=i:
                count += pow(2,j-i,MOD)
        return count%MOD
        