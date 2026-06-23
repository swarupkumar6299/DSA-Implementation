class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        r -= l                          # normalize range to [0, r-l]

        # dp[i][j] = ways to form valid zigzag of length i+1
        #            ending at (normalized) value j
        dp = [[0] * (r + 1) for _ in range(n)]

        # base case: every value is a valid length-1 array
        for j in range(r + 1):
            dp[0][j] = 1

        for i in range(1, n):
            prev = 0

            if i % 2 == 1:                  # odd step → move UP → prefix (left→right)
                for j in range(r + 1):
                    dp[i][j] = prev         # sum of dp[i-1][0..j-1]
                    prev = (prev + dp[i-1][j]) % MOD

            else:                           # even step → move DOWN → suffix (right→left)
                for j in range(r, -1, -1):
                    dp[i][j] = prev         # sum of dp[i-1][j+1..r]
                    prev = (prev + dp[i-1][j]) % MOD

        one_branch_total = sum(dp[-1]) % MOD   # dp[-1] == dp[n-1]
        return (one_branch_total * 2) % MOD    # ×2 for symmetric branch