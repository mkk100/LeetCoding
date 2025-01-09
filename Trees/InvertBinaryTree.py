class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
# Time complexity: O(n)
# Space complexity: O(1)