class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        inf = int(1e9+90)
        
        dp = [[inf for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(m+1):
            dp[n][i] = m - i
        
        for i in range(n+1):
            dp[i][m] = n - i
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j] = min(
                        dp[i+1][j] + 1,
                        dp[i][j+1] + 1,
                        dp[i+1][j+1] + (word1[i] != word2[j])
                    )
                
        return dp[0][0]