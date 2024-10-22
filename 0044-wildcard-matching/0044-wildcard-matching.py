class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1 for _ in range(len(p))]for _ in range(len(s))]
        def helper(index1,index2):
            if index1>=len(s) and index2>=len(p):
                return True
            if index1>=len(s) and index2<len(p):
                while index2<len(p):
                    if p[index2]!="*":
                        return False
                    index2+=1
                return True
            if index2>=len(p):
                return False
            if dp[index1][index2]!=-1:
                return dp[index1][index2]
            if s[index1]==p[index2] or p[index2]=='?':
                dp[index1][index2]= helper(index1+1,index2+1)
            elif s[index1]!=p[index2] and p[index2]!="*":
                dp[index1][index2]=False
            elif p[index2]=='*':
                dp[index1][index2]= helper(index1+1,index2+1) or helper(index1,index2+1) or helper(index1+1,index2)
            return dp[index1][index2]
        return helper(0,0)