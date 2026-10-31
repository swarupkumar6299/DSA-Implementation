MOD = 10**9 + 7

class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        dp = [0] * len(grid[0])
        dp[0] = 1

        for row in grid:
            left = 0
            for j, c in enumerate(row):
                if c:
                    dp[j], left = left, dp[j]
                else:
                    s = left + dp[j]
                    if s >= MOD:
                        s -= MOD
                    dp[j] = left = s

        return left