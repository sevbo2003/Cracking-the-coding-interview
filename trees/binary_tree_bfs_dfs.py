from collections import deque


class Node:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

    def __repr__(self):
        return str(self.val)

    def insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert_node(val)
            elif val >= self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert_node(val)

    @staticmethod
    def insert_nodes(vals: list, root):
        for i in vals:
            root.insert_node(i)

    def bfs(self, root=None):
        # https://csanim.com/tutorials/breadth-first-search-python-visualization-and-code
        if root is None:
            return None
        queue, values = deque(), []
        queue.append(root)

        while queue:
            level_values = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                level_values.append(cur_node.val)

                if cur_node.left is not None:
                    queue.append(cur_node.left)

                if cur_node.right is not None:
                    queue.append(cur_node.right)

            values.append(level_values)

        return values

    def dfs_recursive(self, root=None):
        if root is None:
            return None
        else:
            print(root.val, end=" ")
            self.dfs_recursive(root.left)
            self.dfs_recursive(root.right)


if __name__ == "__main__":
    root = Node(4)
    root.insert_nodes([2, 1, 3, 6, 5, 7], root)  # BST is created.
    print(root.bfs(root))
    root.dfs_recursive(root)
