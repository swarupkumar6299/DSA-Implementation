class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = [(n1,n2) for n1, n2 in zip(nums1, nums2)]
        pair = sorted(pair, key = lambda p: p[1], reverse = True)

        minHeap = []
        n1sum = 0
        res = 0
        for n1, n2 in pair:
            n1sum += n1
            heapq.heappush(minHeap,n1)
            if len(minHeap)>k:
                n1pop = heapq.heappop(minHeap)
                n1sum -= n1pop
            if len(minHeap) == k:
                res = max(res,n1sum * n2)
        return res 
        