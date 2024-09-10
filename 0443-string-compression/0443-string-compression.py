class Solution:
    def compress(self, chars: List[str]) -> int:
        r,i = 0,0
        while(i<len(chars)):
            currChar = chars[i]
            currOcc = 0
            while((i<len(chars))and(chars[i]==currChar)):
                currOcc+=1
                i+=1
            chars[r] = currChar
            r+=1
            if (currOcc>1):
                currOccstr = str(currOcc)
                for j in range(len(currOccstr)):
                    chars[r] = currOccstr[j]
                    r+=1
        return r