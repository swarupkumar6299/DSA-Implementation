class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0

        res = []
        for ch in seq:
            if ch == "(":
                depth += 1
                res += [depth % 2]

            if ch == ")":
                res += [depth % 2]
                depth -= 1
        return res
        