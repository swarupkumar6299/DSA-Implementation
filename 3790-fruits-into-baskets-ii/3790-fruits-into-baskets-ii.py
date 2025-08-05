class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        m = len(baskets)
        # To keep track of which baskets are used
        used = [False] * m
        unplaced = 0
        
        for fruit in fruits:
            placed = False
            for i in range(m):
                if not used[i] and baskets[i] >= fruit:
                    used[i] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        
        return unplaced