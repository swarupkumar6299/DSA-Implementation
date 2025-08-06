import math
import bisect

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.data = [math.inf] * (2 * self.size)
        for i in range(self.n):
            self.data[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.data[i] = min(self.data[2 * i], self.data[2 * i + 1])

    def update(self, pos, value):
        pos += self.size
        self.data[pos] = value
        pos //= 2
        while pos:
            self.data[pos] = min(self.data[2 * pos], self.data[2 * pos + 1])
            pos //= 2

    def query(self, left, right):
        res = math.inf
        left += self.size
        right += self.size
        while left < right:
            if left & 1:
                res = min(res, self.data[left])
                left += 1
            if right & 1:
                right -= 1
                res = min(res, self.data[right])
            left //= 2
            right //= 2
        return res


class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        sorted_baskets = sorted((b, i) for i, b in enumerate(baskets))  # (capacity, original_index)
        basket_indices = [idx for _, idx in sorted_baskets]

        # Map original basket index -> position in sorted_baskets
        index_in_sorted = {orig_idx: pos for pos, (_, orig_idx) in enumerate(sorted_baskets)}

        # Build segment tree with original indices
        seg_tree = SegmentTree(basket_indices)

        placed = 0

        for fruit in fruits:
            # Binary search to find first basket that can fit this fruit
            pos = bisect.bisect_left(sorted_baskets, (fruit, -1))
            if pos == len(sorted_baskets):
                continue  # No basket can fit

            # Query smallest original index among baskets[pos:]
            min_index = seg_tree.query(pos, len(sorted_baskets))
            if min_index == math.inf:
                continue  # All large-enough baskets are used

            # Get position in sorted list directly (O(1))
            used_pos = index_in_sorted[min_index]

            # Mark that basket as used
            seg_tree.update(used_pos, math.inf)
            placed += 1

        return n - placed