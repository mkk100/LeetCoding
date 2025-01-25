# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = 0
        def dfs(node):
            if not node and res != targetSum:
                res = 0
                return 0

            res += dfs(node.left)
            res += dfs(node.right)

            if res == targetSum:
                return True
            return node.val
        return dfs(root)