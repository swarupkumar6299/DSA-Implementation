class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pats = [0] *len(nums)
        start, end = min(L[0] for L in nums), max(L[0] for L in nums)
        for s in sum(nums, []):
            newE = 0
            for L in nums:
                j  = bisect_left(L,s)
                k = bisect_left(L,s + end - start)
                if j >= k:
                    break
                else:
                    newE = max(newE, L[j])
            else:
                start, end = s, newE
        return [start, end]        