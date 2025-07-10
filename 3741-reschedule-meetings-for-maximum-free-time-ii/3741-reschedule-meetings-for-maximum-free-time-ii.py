class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        suffix_max = [0] * len(gaps)
        for i in range(len(gaps)-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], gaps[i+1])

        prefix_max = [0] * len(gaps)
        for i in range(2, len(gaps)):
            prefix_max[i] = max(prefix_max[i-1], gaps[i-2])

        res = 0
        for i in range(1, len(gaps)):
            meeting_time = endTime[i-1] - startTime[i-1]
            if meeting_time <= max(prefix_max[i], suffix_max[i]):
                res = max(res, gaps[i-1] + gaps[i] + meeting_time)
            res = max(res, gaps[i-1] + gaps[i])
        return res


        