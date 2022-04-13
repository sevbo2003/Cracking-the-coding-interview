"""
Input: Tree as array
Output: We give the max depth of tree

Do with DFS (depth first search)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = [root]
        count = 0

        while q:
            for _ in range(len(q)):
                l = q.pop(0)
                if l.left:
                    q.append(l.left)
                if l.right:
                    q.append(l.right)
            count += 1

        return count


node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1, node2, node3)

sol = Solution()
print(sol.maxDepth(node1))

