"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # print(root.left.left.next)

        if not root:
            return root

        q = [root]

        while q:
            curr = q.pop(0)  # taking the left most element from queue
            if curr.left and curr.right:  # Check for children
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                q.append(curr.left)
                q.append(curr.right)

        return root
