class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {i:text.count(i) for i in "balloon"}
        d['l'] = d['l'] // 2
        d['o'] = d['o'] //2
        return min(d.values())