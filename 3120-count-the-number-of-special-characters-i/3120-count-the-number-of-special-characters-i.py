class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        f = collections.Counter(word)

        count = 0
        for c in string.ascii_uppercase:
            if f[c]>0 and f[c.lower()]>0:
                count += 1
        return count
        