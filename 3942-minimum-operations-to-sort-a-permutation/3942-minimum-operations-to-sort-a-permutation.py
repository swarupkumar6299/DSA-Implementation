from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        p = nums.index(0)
        INF = float('inf')
        ans = INF

        # Shape A: rotation of [0..n-1]
        if all(nums[(p + i) % n] == i for i in range(n)):
            ans = min(ans, p, n - p + 2)

        # Shape B: rotation of [n-1..0]
        k = (p + 1) % n
        if all(nums[(k + i) % n] == n - 1 - i for i in range(n)):
            ans = min(ans, 1 + min(k, n - k))

        return -1 if ans == INF else ans