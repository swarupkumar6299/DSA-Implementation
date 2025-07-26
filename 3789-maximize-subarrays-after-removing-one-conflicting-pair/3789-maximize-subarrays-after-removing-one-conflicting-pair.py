class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        valid = 0
        maxLeft = secondMax = 0
        gains = [0] * (n+1)
        conflicts = [[] for _ in range(n+1)]

        for a,b in conflictingPairs:
            if a > b:
                a,b = b,a
            conflicts[b].append(a)

        for r in range(1,n+1):
            for a in conflicts[r]:
                if a > maxLeft:
                    secondMax = maxLeft
                    maxLeft = a
                elif a > secondMax:
                    secondMax = a
            
            valid += (r - maxLeft)
            gains[maxLeft] += (maxLeft - secondMax)

        return valid + max(gains)