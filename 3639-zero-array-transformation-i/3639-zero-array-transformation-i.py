class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        q = [0] * (n + 1)
        for start, end in queries:
            q[start] += 1
            if end + 1 < len(q):
                q[end + 1] -= 1
        for i in range(1, n):
            q[i] += q[i - 1]
        for i in range(n):
            if q[i] < nums[i]:
                return False
        return True
        