class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs (i):
            visited[i] = True
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and not visited[j]:
                    dfs(j)
        provinces = 0
        visited = [False]*len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                provinces += 1 
                dfs(i)

        return provinces       