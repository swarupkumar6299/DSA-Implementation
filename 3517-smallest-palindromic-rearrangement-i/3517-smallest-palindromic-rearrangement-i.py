class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        return  ''.join(
            (half:= [k*(v//2) for k,v in sorted(cnt.items())]) + 
            ([""] if len(s)&1 == 0  else [s[(len(s)+1)//2 -1]]) + 
            half[::-1]
        )
        