class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m) ]
        def dfs(i, j):
            if not(0<=i<m and 0<=j<n) or grid[i][j]==0 or visited[i][j]:
                return 0

            visited[i][j] = True
            return grid[i][j] + dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)

        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0 and not visited[i][j]:
                    v = dfs(i, j)
                    if v%k==0:
                        res += 1
        
        return res