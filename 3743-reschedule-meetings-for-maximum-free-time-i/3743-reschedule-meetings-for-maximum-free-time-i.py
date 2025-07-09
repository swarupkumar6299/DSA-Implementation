class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1]) #arrays of gap windows between meetings
        #last gap
        gaps.append(eventTime - endTime[-1])
        s = min(k+1, len(gaps))
        cur = sum(gaps[:s])
        res = cur
        for i in range(s, len(gaps)):
            cur += gaps[i] - gaps[i-s]
            res = max(res, cur)
        return res


        