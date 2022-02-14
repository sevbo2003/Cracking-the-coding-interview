"""
Breadth first search

BFS Queue
DFS Stack

The traversal searches at root node,
then we visit the neighbours this node.

Using Breadth First Seach

Input: Tree
Output: Array of the BFS
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        """
        We have root
        then root has left and right
        we check for both left an right, then append them, then append again to big list
        """
        if not root:
            return []

        next, result_list = [], []
        next.append(root)

        while len(next):
            nodes_values = []

            for _ in range(len(next)):
                node = next.pop(0)
                nodes_values.append(node.val)

                if node.left:
                    next.append(node.left)

                if node.right:
                    next.append(node.right)

            result_list.append(nodes_values)

        return result_list
