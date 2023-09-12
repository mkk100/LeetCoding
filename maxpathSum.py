class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax,0)
            rightmax = max(rightmax,0)

            res[0] = max(res[0], root.val + leftmax + rightmax)

            return root.val + max(leftmax , rightmax)
        dfs(root)
        return res[0]