import itertools

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(itertools.accumulate([0] + gain))