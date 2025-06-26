class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        val = 0
        power = 1
        n = len(s)

        for i in range(n-1,-1,-1):
            if s[i]=='0':
                count +=1
            else:
                if power <= k and val + power <= k:
                    val += power
                    count += 1
            power <<=1
        return count