# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            max_val = self.findMax(root.left)
            root.val = max_val

            root.left = self.deleteNode(root.left,max_val)
        return root

    def findMax(self,node:TreeNode)-> int:
        while node.right is not None:
            node = node.right
        return node.val