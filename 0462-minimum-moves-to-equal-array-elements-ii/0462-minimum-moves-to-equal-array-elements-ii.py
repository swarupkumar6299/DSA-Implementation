class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        len_arr = len(nums)
        if len_arr % 2 != 0:
            median_elem = nums[len_arr//2]
        else:
            median_elem = (nums[len_arr//2-1] + nums[len_arr//2]) // 2

        ans = sum(abs(x - median_elem) for x in nums)
        return ans
        