# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the root is None or if we find either p or q
        if not root or root == p or root == q:
            return root
        
        # Recursively search the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        
        # Recursively search the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, this is the LCA
        if left and right:
            return root
        
        # Otherwise return either left or right, whichever is non-null
        return left if left else right
