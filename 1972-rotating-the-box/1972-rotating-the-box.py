from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(box), len(box[0])
        
        # Process each row to simulate gravity
        for r in range(ROWS):
            i = COLS - 1  # Pointer for the next empty space
            for c in reversed(range(COLS)):
                if box[r][c] == "#":
                    # Move the stone to the farthest available empty space
                    box[r][i], box[r][c] = box[r][c], box[r][i]
                    i -= 1
                elif box[r][c] == "*":
                    # Reset the pointer when hitting an obstacle
                    i = c - 1
        
        # Rotate the box 90 degrees clockwise
        res = []
        for c in range(COLS):
            col = []
            for r in reversed(range(ROWS)):
                col.append(box[r][c])
            res.append(col)
        
        return res
