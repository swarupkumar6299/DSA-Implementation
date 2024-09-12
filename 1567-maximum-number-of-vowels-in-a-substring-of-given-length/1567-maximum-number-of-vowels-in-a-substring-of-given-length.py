class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        l, cnt, res = 0, 0, 0
        for r in range(len(s)):
            cnt += 1 if s[r] in vowel else 0
            if r - l + 1 > k:  # Correct indentation here
                if s[l] in vowel:
                    cnt -= 1
                l += 1
            res = max(res, cnt)
        return res
