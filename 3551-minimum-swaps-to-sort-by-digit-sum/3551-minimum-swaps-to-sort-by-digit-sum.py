class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        n = len(nums)
        # Create target sorted arrangement based on (digit_sum, value)
        sorted_arr = sorted((get_digit_sum(x), x) for x in nums)
        
        # Map each value to its target index
        target_pos = {val: i for i, (_, val) in enumerate(sorted_arr)}
        
        # Count permutation cycles
        vis = [False] * n
        ans = n
        
        for i in range(n):
            if not vis[i]:
                ans -= 1
                j = i
                while not vis[j]:
                    vis[j] = True
                    j = target_pos[nums[j]]
                    
        return ans