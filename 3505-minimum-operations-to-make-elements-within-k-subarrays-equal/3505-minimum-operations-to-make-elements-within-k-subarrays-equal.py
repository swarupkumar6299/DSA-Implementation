from heapq import heappush, heappop
from collections import Counter

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Phase 1: Precalculate the minimum cost to make each window of size x equal.
        # cost[i] will store the operations required for the subarray nums[i : i + x]
        window_costs = [float('inf')] * n
        
        # Two-heap / Lazy-deletion approach to maintain sliding window median
        left_max_heap = []   # Lower half (inverted for max-heap behavior)
        right_min_heap = []  # Upper half
        
        left_sum = 0
        right_sum = 0
        
        left_size = 0
        right_size = 0
        
        # Track elements that need to be lazily deleted from the heaps
        del_left = Counter()
        del_right = Counter()
        
        def balance():
            nonlocal left_sum, right_sum, left_size, right_size
            # Keep left_size == right_size (if x is even) or left_size == right_size + 1 (if x is odd)
            target_left = (x + 1) // 2
            
            # Move from left to right if left is too large
            while left_size > target_left:
                while left_max_heap and del_left[-left_max_heap[0]] > 0:
                    del_left[-left_max_heap[0]] -= 1
                    heappop(left_max_heap)
                val = -heappop(left_max_heap)
                left_sum -= val
                left_size -= 1
                heappush(right_min_heap, val)
                right_sum += val
                right_size += 1
                
            # Move from right to left if left is too small
            while left_size < target_left and right_size > 0:
                while right_min_heap and del_right[right_min_heap[0]] > 0:
                    del_right[right_min_heap[0]] -= 1
                    heappop(right_min_heap)
                val = heappop(right_min_heap)
                right_sum -= val
                right_size -= 1
                heappush(left_max_heap, -val)
                left_sum += val
                left_size += 1
                
            # Clean up stale elements at the top of the heaps
            while left_max_heap and del_left[-left_max_heap[0]] > 0:
                del_left[-left_max_heap[0]] -= 1
                heappop(left_max_heap)
            while right_min_heap and del_right[right_min_heap[0]] > 0:
                del_right[right_min_heap[0]] -= 1
                heappop(right_min_heap)

        def add_num(val):
            nonlocal left_sum, right_sum, left_size, right_size
            if not left_max_heap or val <= -left_max_heap[0]:
                heappush(left_max_heap, -val)
                left_sum += val
                left_size += 1
            else:
                heappush(right_min_heap, val)
                right_sum += val
                right_size += 1
            balance()

        def remove_num(val):
            nonlocal left_sum, right_sum, left_size, right_size
            if val <= -left_max_heap[0]:
                del_left[val] += 1
                left_sum -= val
                left_size -= 1
            else:
                del_right[val] += 1
                right_sum -= val
                right_size -= 1
            balance()

        # Build initial window
        for i in range(x):
            add_num(nums[i])
        
        # Calculate cost for the first window
        median = -left_max_heap[0]
        window_costs[0] = (median * left_size - left_sum) + (right_sum - median * right_size)
        
        # Slide window across the array
        for i in range(x, n):
            remove_num(nums[i - x])
            add_num(nums[i])
            median = -left_max_heap[0]
            window_costs[i - x + 1] = (median * left_size - left_sum) + (right_sum - median * right_size)

        # Phase 2: DP to choose K non-overlapping subarrays
        # dp[j] represents the minimum operations required to build `j` equal subarrays
        dp = [float('inf')] * (k + 1)
        dp[0] = 0
        
        # To strictly prevent overlapping, we maintain the choices state transitioning element by element
        # dp_next dynamically tracks updates at the current element boundary
        new_dp = [float('inf')] * (k + 1)
        
        # We can also optimize using a standard 2D formulation or 1D rolling array with history tracking
        # Let's use a clear historical window lookup structure:
        # history[i][j] = min operations using first `i` elements to get `j` subarrays
        history = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            history[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Option A: Do not start a window ending at i-1
                history[i][j] = history[i - 1][j]
                
                # Option B: Form a window ending at i-1 (starts at i-x)
                if i >= x and window_costs[i - x] != float('inf'):
                    history[i][j] = min(history[i][j], history[i - x][j - 1] + window_costs[i - x])
                    
        return history[n][k]
