# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def traverse(root):
            if not root:
                return
            if val > root.val:
                return traverse(root.right)
            elif val < root.val:
                return traverse(root.left)
            else:
                return root
        return traverse(root)
            