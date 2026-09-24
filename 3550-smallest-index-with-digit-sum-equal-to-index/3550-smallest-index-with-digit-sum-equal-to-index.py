class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if sum(map(int,list(str(nums[i])))) == i:
                return i
        return -1
        