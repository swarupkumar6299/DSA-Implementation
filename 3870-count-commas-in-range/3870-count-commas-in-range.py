class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        res = 0
        lis = [1]*8
        for i in range(1,len(lis)):
            lis[i] = lis[i-1]*1000
            curr = lis[i]
            if i == 1: continue
            if lis[i]>n and n>= lis[i-1]:
                res += (n-lis[i-1])*(i-1)+1
                break
            elif n >= lis[i]:
                res += (lis[i]-lis[i-1])*(i-1)+1
        return res
        