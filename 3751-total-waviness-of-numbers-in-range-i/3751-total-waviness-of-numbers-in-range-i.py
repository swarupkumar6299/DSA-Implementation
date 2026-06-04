class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        op =0
        for i in range(num1,num2+1):
            s = str(i)
            if len(s) < 3:
                continue
            for j in range(1,len(s)-1):
                p = int(s[j-1])
                q = int(s[j])
                r = int(s[j+1])
                if p<q>r or p>q<r:
                    op+=1
        return op