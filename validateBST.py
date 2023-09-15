class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validateBST(root,left,right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            return (validateBST(root.left, left, root.val) and validateBST(root.right,root.val,right))
        return validateBST(root,float("-inf"),float("inf"))