class Solution:
    def minSwaps(self, s: str) -> int:
        unmatch = 0
        for character in s:
            unmatch += 1 if character == '[' else -1 if unmatch > 0 else 0
        return (unmatch+1)//2
        