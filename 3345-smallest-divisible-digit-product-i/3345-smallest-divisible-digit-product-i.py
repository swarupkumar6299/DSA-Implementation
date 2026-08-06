class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n,n+11):
            prod = 1
            smIdx = num
            while smIdx>0:
                prod *= smIdx%10
                smIdx//=10
            if prod%t==0:
                return num