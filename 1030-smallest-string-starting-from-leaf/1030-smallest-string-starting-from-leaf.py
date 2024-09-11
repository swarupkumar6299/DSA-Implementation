class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node, cur):
            if not node:
                return "~"  # Return a large value for comparison.
            
            cur = chr(ord('a') + node.val) + cur  # Prepend current character
            
            # If it's a leaf node, return the current string.
            if not node.left and not node.right:
                return cur
            
            # Recur for left and right subtrees and return the smaller string.
            left = helper(node.left, cur)
            right = helper(node.right, cur)
            return min(left, right)

        return helper(root, "")
