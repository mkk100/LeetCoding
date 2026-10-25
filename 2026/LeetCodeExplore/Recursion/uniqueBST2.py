# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        def generate(l, r):
            if l > r:
                return [None]
            
            res = []
            for val in range(l, r + 1):
                for ltree in generate(l, val - 1):
                    for rtree in generate(val + 1, r):
                        root = TreeNode(val, ltree, rtree)
                        res.append(root)
            return res
        return generate(1, n)
                        