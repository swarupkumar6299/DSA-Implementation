class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        dct = defaultdict(int)
        mn = inf

        for b in basket1:
            dct[b] += 1
            mn = min(mn, b)
        for b in basket2:
            dct[b] -= 1
            mn = min(mn, b)
        
        lst = []
        for k, v in dct.items():
            if v % 2 != 0:
                return -1
            for i in range(0, abs(v) // 2):
                lst.append(k)
        
        lst.sort()
        n = len(lst)
        total = 0

        for i in range(0, n // 2):
            total += min(lst[i], mn * 2)
        
        return total