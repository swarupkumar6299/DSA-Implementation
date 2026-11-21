class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        N = len(parent)
        tree = defaultdict(list)
        for v, u in enumerate(parent):
            tree[u].append(v)

        ans = [0] * N
        # Tracks active ancestors on the current DFS path grouped by character
        ancestors = defaultdict(list)

        def dfs(curr: int) -> int:
            size = 1
            color = s[curr]
            
            # Find the closest ancestor with the same character
            ancestor = ancestors[color][-1] if ancestors[color] else -1
            ancestors[color].append(curr)

            for child in tree[curr]:
                size += dfs(child)

            ancestors[color].pop() # not needed anymore, old one
            
            # update current size of this root subtree
            ans[curr] += size
    
            # If no matching ancestor, stay attached to original parent
            if ancestor == -1:
                return ans[curr]
            
            # Otherwise, detach from original parent (return 0) and 
            # transfer entire subtree size to the closest matching ancestor
            ans[ancestor] += ans[curr]
            return 0

        dfs(0)
        return ans