"""
LeetCode Alternative: https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Problem: Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Input:
Output:

SOLUTION 1:
    -
    -
    - Time: O()
    - Space: O()
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(node):
            if node:
                result.append(node.val)
                for child in node.children:
                    dfs(child)

        dfs(root)
        return result
