class Solution:
    # nums[i] = nums[i] & nums[j], nums[j] = nums[i] | nums[j]
    # do this any number of times to maximize sum of squares of k elements
    # changes: (1 in a, 0 in b) --> 1 in b
    #   - so change ONLY happens when 1 in a, 0 in b, and we simply swap those bits
    #   - problem restated: maximum sum of squares swapping a set bit from i to j
    # i does NOT have to be less than j, so we can swap forward or backwards
    #   - this means we can arbitrarily construct a number using 1s from any position in the array
    # NOTE: why does the problem ask for squares? 
    #   - a sum is linear which means it will never change accross addition
    #   - squares are not linear, which allows this problem to exist
    def maxSum(self, nums: List[int], k: int) -> int:
        set_bits = [0] * 30
        mod = 10**9 + 7
        for num in nums:
            for i in range(30):  # 32 works fine. 30 is better bc nums[i] ≤ 10^9 and 10^9 < 2^30
                set_bits[i] += (num >> i) & 1
        
        ans = 0
        for nums_built in range(k):
            cur = 0  # we'll greedily maximize cur using set bits
            for i in range(30):
                # take any remaining bits we can at this position (we run out after building as many nums as 1s at that pos)
                cur |= (set_bits[i] > nums_built) << i 
            ans = (ans + cur * cur) % mod
        return ans
            