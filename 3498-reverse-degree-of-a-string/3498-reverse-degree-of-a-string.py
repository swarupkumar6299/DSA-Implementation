class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for ind,i in enumerate(s):
            x = ord(i) - ord('a') + 1
            y = 27 - x

            sum += (ind+1) * y
        return sum 
        