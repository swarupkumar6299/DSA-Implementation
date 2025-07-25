class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums = list(set(nums))
        max_num, max_sum = -inf, 0
        for num in nums:
            max_num = max(max_num,num)
            max_sum = max(max_sum,num+max_sum)
        return max_num if max_num <1 else max_sum