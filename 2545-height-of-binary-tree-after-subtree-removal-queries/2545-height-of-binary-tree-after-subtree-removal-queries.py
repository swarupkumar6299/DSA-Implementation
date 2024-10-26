# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        par = {} # keep track of parent nodes
        height = {} # height for each node
        
        def dfs(node, level):
            if not node:
                return
            height[node.val] = level
            if node.left:
                par[node.left.val] = node.val
                dfs(node.left, level+1)
            if node.right:
                par[node.right.val] = node.val
                dfs(node.right, level+1)
        
        dfs(root, 0)
        
        # Topological sort
        deg = defaultdict(int)
        for k in par:
            deg[par[k]] += 1
        # starts from leaf nodes    
        q = [k for k in height if not deg[k]]
        h = height.copy() # propagate depth to parent nodes
            
        while q:
            cur = q.pop()
            if cur not in par: continue
            p = par[cur]
            deg[p] -= 1
            h[p] = max(h[p], h[cur])
            if not deg[p]:
                q.append(p)
        
        # for each level, only store top 2 nodes with deepest path
        h_node = defaultdict(list)
        for k in height:
            heappush(h_node[height[k]], (h[k], k))
            if len(h_node[height[k]]) > 2:
                heappop(h_node[height[k]])
        
        
        ans = []
        for q in queries:
            # if current level only one node then whole level gone, the height will minus 1
            if len(h_node[height[q]]) == 1:
                ans.append(height[q] - 1)
            # if deleted node equals the node with deepest path at current level, then chose the second deepest
            elif q == h_node[height[q]][1][1]:
                ans.append(h_node[height[q]][0][0])
            # otherwise select the top one
            else:
                ans.append(h_node[height[q]][1][0])

        
        return ans