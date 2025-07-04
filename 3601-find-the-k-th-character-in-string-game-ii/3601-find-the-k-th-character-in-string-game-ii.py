class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        def dfs(i, k):
            # the 0th character is always 'a'
            if k == 0:
                return 0

            # we're in the 'left half' of the string
            # (we came directly from the previous step)
            if k < (1 << i):
                return dfs(i - 1, k)
            # we're in the 'right half' of the string
            # (we came from some transformation of the previous step)
            else:
                return dfs(i - 1, k - (1 << i)) + operations[i]

        depth = floor(log2(k - 1)) if k > 1 else 0
        dig = dfs(depth, k - 1)
        return chr(ord('a') + dig % 26)