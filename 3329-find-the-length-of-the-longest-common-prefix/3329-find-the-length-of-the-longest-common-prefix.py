class TrieNode:
    def __init__(self):
        self.children = {}
    def insert(self, s: str):
        node = self
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
    def prefix(self, s: str) -> int:
        node = self
        length = 0
        for ch in s:
            if ch not in node.children:
                break
            node = node.children[ch]
            length += 1
        return length
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = TrieNode()
        for num in arr1:
            trie.insert(str(num))
        max_len = 0
        for num in arr2:
            max_len = max(max_len, trie.prefix(str(num)))
        return max_len