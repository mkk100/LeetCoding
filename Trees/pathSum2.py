# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, val):
            if not root:
                return False
            if not root.left and not root.right and root.val - targetSum == 0:
                return True

            left = dfs(root.left, targetSum - root.val)
            right = dfs(root.right, targetSum - root.val)
            return left or right

        dfs(root, targetSum)
