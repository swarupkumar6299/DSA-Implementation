class Solution:
    def kthCharacter(self, k: int) -> str:
        # Initialize the string with 'a'
        word = "a"
        
        # Continue generating the string until it has at least k characters
        while len(word) < k:
            # Generate the next sequence by changing each character to its next one
            next_word = ''.join(chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in word)
            word += next_word
        
        # Return the k-th character (1-indexed)
        return word[k - 1]

# Example usage:
sol = Solution()
k = 5
print(sol.kthCharacter(k))  # Output should be 'b'
        