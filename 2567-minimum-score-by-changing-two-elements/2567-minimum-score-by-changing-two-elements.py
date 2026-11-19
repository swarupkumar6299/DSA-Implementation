import heapq

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        smallest = heapq.nsmallest(3, nums)
        largest = heapq.nlargest(3, nums)

        return min(
            largest[0] - smallest[2],
            largest[1] - smallest[1],
            largest[2] - smallest[0]
        )