class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # We need the 3 largest numbers
        # heapq.nlargest is an optimized O(N log K) operation
        max_three = heapq.nlargest(3, nums)
        
        # We need the 2 smallest numbers
        min_two = heapq.nsmallest(2, nums)
        
        # Case 1: Three largest
        # Case 2: Two smallest * largest
        return max(
            max_three[0] * max_three[1] * max_three[2],
            min_two[0] * min_two[1] * max_three[0]
        )