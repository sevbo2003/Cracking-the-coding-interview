"""
Node Depth

Problem:
    Given the binary tree, find the depth for each node, add up them, and return sum.
    Depth is the distance between root till node.
"""
from collections import deque

from AlgoExpert.tree import TreeNode, build_tree


# Solution #1: DFS
def node_depth_dfs(root: TreeNode) -> int:
    """
    O(N) time | O(H) space, where N is the number of nodes, H is height.

    - Implement DFS algorith and use global sum variable
    """
    sum_ = 0

    def dfs(node, counter=0):
        if node:
            nonlocal sum_
            sum_ += counter
            counter += 1

            dfs(node.left, counter)
            dfs(node.right, counter)

    dfs(root)
    return sum_


# Solution #2: BFS
def node_depth_bfs(root: TreeNode) -> int:
    _sum = 0
    _counter = 0
    queue = deque()
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            _sum += _counter
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        _counter += 1

    return _sum


def main():
    tree = build_tree([100, 50, 200, 25, 75, 90, 300])  # 11
    print('>>', node_depth_bfs(tree))


if __name__ == "__main__":
    main()
