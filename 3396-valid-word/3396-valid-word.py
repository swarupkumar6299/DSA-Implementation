class Solution:
    def isValid(self, word: str) -> bool:
        # Condition 1: Minimum length should be 3
        if len(word) < 3:
            return False
        vowels = "aeiouAEIOU"
        count_of_vowel = 0
        count_of_consonant = 0

        for ch in word:
            if ch in vowels:
                count_of_vowel += 1
            elif ch.isalpha() and ch not in vowels :
                count_of_consonant += 1
            elif ch.isdigit():
                continue # digits are allowed, but don't affect vowel/  consonant count
            else:
                return False # special characters are not allowed
                # Condition 2: At least one vowel and one consonant

        return count_of_vowel >= 1 and count_of_consonant >= 1
            

        