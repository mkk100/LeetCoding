# recursive

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(root, h):
            if not root:
                return 0
            return 1 + max(dfs(root.left, h + 1), dfs(root.right, h + 1))
        
        return dfs(root, 0)
            

# bfs
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = 0
        q = deque()
        if root: q.append(root)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res += 1
        return res

# postorder traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        res, stack = 0, [(root, 1)]
        
        while stack:
            node, height = stack.pop()
            res = max(res, height)
            if node.left: stack.append((node.left, height + 1))
            if node.right: stack.append((node.right, height + 1))
            
        return res