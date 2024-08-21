import sys

class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[sys.maxsize] * n for _ in range(n)]
        
        for l in range(1, n + 1):  # l is the length of the substring
            for i in range(n - l + 1):  # i is the starting index of the substring
                j = i + l - 1  # j is the ending index of the substring
                if l == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i + 1][j] + 1
                    for k in range(i + 1, j + 1):
                        if s[i] == s[k]:
                            dp[i][j] = min(dp[i][j], dp[i][k - 1] + (dp[k + 1][j] if j > k else 0))
        
        return dp[0][n - 1]
