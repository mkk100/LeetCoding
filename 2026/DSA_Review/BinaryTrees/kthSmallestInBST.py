# inorder bst always give you a sorted array

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        res = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res[k - 1]
# recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def dfs(root):
            if not root:
                return root
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res[k-1]