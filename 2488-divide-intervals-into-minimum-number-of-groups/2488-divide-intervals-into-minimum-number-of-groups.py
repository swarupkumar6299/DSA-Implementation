class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        heap = []
        for (start, end) in intervals:
            if heap and start>heap[0]:
                max_end=max(heapq.heappop(heap), end)
                heapq.heappush(heap, max_end)
            else:
                heapq.heappush(heap, end)
        return len(heap)

        