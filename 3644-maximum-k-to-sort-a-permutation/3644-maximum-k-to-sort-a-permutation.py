class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        if nums[0] != 0: return 0
        ans = ~ 0  # the bitwise complement of zero

        for idx, num in enumerate(nums):
            if num == idx: continue
            ans&= num

        return ans if ans > 0 else 0