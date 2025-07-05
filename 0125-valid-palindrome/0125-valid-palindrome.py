class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Check if it's equal to its reverse
        return cleaned == cleaned[::-1]
        