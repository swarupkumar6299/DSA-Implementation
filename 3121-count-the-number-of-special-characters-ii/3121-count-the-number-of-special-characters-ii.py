class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        N = len(word)

        first = {}
        last = {}
        for i,c in enumerate(word):
            if c.isupper():
                c = c.lower()
                if c not in first:
                    first[c]=i
            else:
                last[c]=i

        count = 0
        for c in string.ascii_lowercase: 
            if c in first and c in last and last[c] < first[c]:
                count +=1
        return count
    
        