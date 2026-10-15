class Solution:
    def sumCounts(self, a: List[int]) -> int:
        r = range(len(a));return sum(len({*a[i:j+1]})** 2for i in r for j in r)
        