from collections import defaultdict
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        m=10**9+7
        def mat_mult(a,b):
            res=[[0]*26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    for k in range(26):
                        res[i][j]=(res[i][j]+a[i][k]*b[k][j])%m
            return res
        def mat_pow(mat,p):
            res=[[int(i==j) for j in range(26)] for i in range(26)]
            while p:
                if p&1:
                    res=mat_mult(res,mat)
                mat=mat_mult(mat,mat)
                p>>=1
            return res
        T=[[0]*26 for _ in range(26)]
        for i in range(26):
            for j in range(nums[i]):
                T[i][(i+j+1)%26]+=1
        T=mat_pow(T,t)
        r=0
        for ch in s:
            idx=ord(ch)-ord('a')
            r=(r+sum(T[idx]))%m
        return r