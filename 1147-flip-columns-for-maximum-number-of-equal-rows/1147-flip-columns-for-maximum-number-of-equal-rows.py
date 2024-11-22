class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        for row in matrix:
            h = tuple(row) if row[0] else tuple(1-x for x in row)
            if h in d:
                d[h] +=1
            else:
                d[h] = 1
        return max(d.values())
