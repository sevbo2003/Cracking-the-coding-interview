"""
Given the tree, return True if tree has the sum of paths == targetSum, else False.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.is_target_found = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(root, sum_):
            if root:
                sum_ += root.val
                if not root.left and not root.right:
                    if sum_ == targetSum:
                        self.is_target_found = True

                traversal(root.right, sum_)
                traversal(root.left, sum_)

        traversal(root, 0)
        return self.is_target_found


class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def traversal(root, sum_):
            if root:
                sum_ += root.val
                if not root.left and not root.right:
                    return sum_ == targetSum

                return traversal(root.right, sum_) or traversal(root.left, sum_)

        return traversal(root, 0)
