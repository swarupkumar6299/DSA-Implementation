

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        
        def time_to_min(t):
            h, m = map(int, t.split(":"))
            return 60 * h + m
        
        n = len(timePoints)
        # Convert all times to minutes
        minutes = [time_to_min(time) for time in timePoints]
        
        # Add a circular comparison: the first and the last time (next day for circular difference)
        res = 24 * 60 - (minutes[-1] - minutes[0])
        
        # Compare consecutive time points
        for i in range(n - 1):
            res = min(res, minutes[i + 1] - minutes[i])
        
        return res
