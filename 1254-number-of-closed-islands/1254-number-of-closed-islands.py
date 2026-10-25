class UnionFind:
    def __init__(self, n: int):
        # Keeps track of the total number of independent sets.
        # Initially, every single cell is treated as a separate set.
        self.cnt_sets = n
        self.parent = [*range(n)]
        self.rank = [1] * n
               
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        # If they share the same root, they are already in the same set.
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        # Successfully merged two sets, decrement the total set count.
        self.cnt_sets -= 1
        

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # Initialize UnionFind with m * n elements (one for each cell in the grid).
        uf = UnionFind(m * n)
        
        # Traverse the entire grid using a flat coordinates approach
        for x, (i, j) in enumerate(product(range(m), range(n))):
           
            # Key Logic: Forcefully merge all water cells ('1') and all boundary land cells 
            # into a single global "outer/invalid" component represented by index 0.
            if i in (0, m-1) or j in (0, n-1) or grid[i][j] == 1:
                uf.union(0, x)
            
            # If the current cell is internal land ('0'), check its right and bottom neighbors.
            if grid[i][j] == 0:
                # Connect with the neighbor below if it is also land
                if i + 1 < m and grid[i+1][j] == 0:
                    uf.union(x, x + n)
                # Connect with the neighbor to the right if it is also land
                if j + 1 < n and grid[i][j+1] == 0:
                    uf.union(x, x + 1)
                    
        # Total valid closed islands = total remaining sets minus 1.
        # The subtracted '1' accounts for the massive combined set of all water and boundary components.
        return uf.cnt_sets - 1