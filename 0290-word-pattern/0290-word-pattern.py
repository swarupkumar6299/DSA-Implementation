class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        words = words.split(" ")
        if len(pattern)!= len(words):
            return False
        charToWord = {}
        wordToChar = {}
        for c, w in zip(pattern,words):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] !=c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True

        