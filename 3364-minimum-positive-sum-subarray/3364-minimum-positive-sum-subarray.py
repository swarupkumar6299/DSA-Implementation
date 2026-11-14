from sortedcontainers import SortedList

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = inf 
        prefix = list(accumulate(nums, initial=0))
        sl = SortedList()
        for i in range(len(nums)): 
            if i >= l-1: sl.add(prefix[i-l+1])
            if i >= r: sl.remove(prefix[i-r])
            k = sl.bisect_left(prefix[i+1])-1
            if k >= 0: ans = min(ans, prefix[i+1] - sl[k])
        return ans if ans < inf else -1