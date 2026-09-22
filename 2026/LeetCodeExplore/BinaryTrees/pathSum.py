# My initial approach

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        
        def dfs(root, total):
            if not root:
                return False
            
            total += root.val
            if total == targetSum and not root.left and not root.right:
                return True

            
            l = dfs(root.left, total)
            r = dfs(root.right, total)
            return l or r
            
        return dfs(root, 0)

# neetcode has the same approach           
            