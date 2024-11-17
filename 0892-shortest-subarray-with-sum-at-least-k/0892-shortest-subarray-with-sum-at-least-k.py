class Solution:
    # Complexity:
    # Time O(N) and Space O(N) where N is the length of nums.
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        result = len(nums) + 1
        prefix_sum = 0
        left_prefixes = deque() # Prefix(endInclusive, sum)
        left_prefixes.append([-1, prefix_sum])  

        for right, num in enumerate(nums):
            prefix_sum += num
            max_left_sum = prefix_sum - k

            while left_prefixes and left_prefixes[0][1] <= max_left_sum:
                left = left_prefixes.popleft()[0]
                result = min(result, right - left)

            while left_prefixes and prefix_sum <= left_prefixes[-1][1]:
                left_prefixes.pop()
            left_prefixes.append([right, prefix_sum])
        return -1 if len(nums) < result else result