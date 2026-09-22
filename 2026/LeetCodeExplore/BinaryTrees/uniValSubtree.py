class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def count_unival_subtrees(self, root):
        res = 0
        if not root:
            return 0
        
        def dfs(past_val, root):
            nonlocal res
            if not root:
                return past_val

            if dfs(root.val, root.left) == dfs(root.val, root.right):
                res += 1

            return root.val
        dfs(root.val, root)
        return res


# -------------------------
# Test cases
# -------------------------

def test1():
    #     5
    #    / \
    #   1   5
    #      / \
    #     5   5
    #
    # Unival subtrees:
    # left 1
    # bottom-left 5
    # bottom-right 5
    # right subtree 5,5,5
    #
    # Answer = 4

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(5)

    return root, 4


def test2():
    #       1
    #      / \
    #     1   1
    #    / \
    #   1   1
    #
    # Every subtree is unival.
    # Answer = 5

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    return root, 5


def test3():
    #     1
    #    / \
    #   2   3
    #
    # Each leaf is unival.
    # Answer = 2

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    return root, 2


def test4():
    # Single node
    #
    # Answer = 1

    root = TreeNode(1)

    return root, 1


def test5():
    # Empty tree
    #
    # Answer = 0

    return None, 0


def test6():
    #     5
    #    /
    #   5
    #  /
    # 5
    #
    # Every subtree is unival.
    # Answer = 3

    root = TreeNode(5)
    root.left = TreeNode(5)
    root.left.left = TreeNode(5)

    return root, 3


# -------------------------
# Run tests
# -------------------------

solution = Solution()

tests = [
    test1(),
    test2(),
    test3(),
    test4(),
    test5(),
    test6(),
]

for i, (root, expected) in enumerate(tests, 1):
    actual = solution.count_unival_subtrees(root)

    print(
        f"Test {i}: "
        f"expected={expected}, "
        f"actual={actual}, "
        f"{'PASS' if actual == expected else 'FAIL'}"
    )