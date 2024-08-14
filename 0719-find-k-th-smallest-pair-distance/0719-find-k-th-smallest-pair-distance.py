class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sort the array to allow binary search and sliding window techniques
        nums.sort()
        
        # Helper function to count pairs with distance <= mid
        def count_pairs(mid):
            count, j = 0, 0
            for i in range(len(nums)):
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            return count
        
        # Binary search on the distance
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low
