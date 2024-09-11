class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def insert(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                left_node = TreeNode(val)
                right_node = TreeNode(val)
                
                left_node.left = node.left
                right_node.right = node.right
                
                node.left = left_node
                node.right = right_node
            else:
                insert(node.left, current_depth + 1)
                insert(node.right, current_depth + 1)
        
        insert(root, 1)
        return root
