from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        # Step 1: count fresh oranges and enqueue rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        # Directions for 4-way BFS (up, down, left, right)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Step 2: Perform BFS
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Check if the new position is within bounds and if it's a fresh orange
                    if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1:
                        continue

                    # Rotten the fresh orange
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            # Increment the time after each level of BFS
            time += 1

        # If there are still fresh oranges, return -1, otherwise return the time
        return time if fresh == 0 else -1
