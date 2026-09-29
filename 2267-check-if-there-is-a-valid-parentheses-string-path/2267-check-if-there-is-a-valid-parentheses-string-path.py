class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        @lru_cache(maxsize=None)
        def hasValidPathInner(x,y,cnt):
            if x == m or y == n or cnt < 0:
                return False
            cnt += 1 if grid[x][y] == '(' else -1

            if x == m -1 and y == n - 1 and not cnt:
                return True
            return hasValidPathInner(x + 1, y, cnt) or hasValidPathInner(x,y+1,cnt)
        return hasValidPathInner(0,0,0)
        