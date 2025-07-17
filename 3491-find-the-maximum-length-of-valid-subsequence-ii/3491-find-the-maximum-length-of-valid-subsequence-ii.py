class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0]  * k for _ in range(k)]
        for n in nums:
            n%=k
            for i in range(k):
                dp[i][n] = dp[n][i]+1
        return max(max(x)for x in dp)