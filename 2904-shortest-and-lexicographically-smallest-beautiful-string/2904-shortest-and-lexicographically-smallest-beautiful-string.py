class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        ans = []
        min_string = ""
        count =0
        for r in range(len(s)):
            if s[r] == '1':
                count += 1
                while count ==k:
                    ans = (s[l:r+1])
                    if min_string == "" or len(ans) < len(min_string) or (len(ans) == len(min_string) and ans < min_string):
                        min_string = ans
                    if s[l] == '1':    
                        count -= 1
                    l+=1
        return min_string
        
            
            

        