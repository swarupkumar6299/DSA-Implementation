class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Convert to sets for O(1) lookups
        guards_set = {tuple(guard) for guard in guards}
        walls_set = {tuple(wall) for wall in walls}
        visible_set = set()

        # Directions: left, right, up, down
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Helper function for directional traversal
        def mark_visible(row: int, col: int, drow: int, dcol: int):
            while 0 <= row < m and 0 <= col < n:
                if (row, col) in guards_set or (row, col) in walls_set:
                    break
                visible_set.add((row, col))
                row += drow
                col += dcol

        # Traverse in all directions for each guard
        for row, col in guards_set:
            for drow, dcol in directions:
                mark_visible(row + drow, col + dcol, drow, dcol)

        # Calculate unguarded cells
        full_set = {(i, j) for i in range(m) for j in range(n)}
        unguarded_cells = full_set - guards_set - walls_set - visible_set

        return len(unguarded_cells)