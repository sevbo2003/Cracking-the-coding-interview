# [Trees](https://github.com/Rustam-Z/data-structures-and-algorithms#tree)

Questions to raise during coding interview:
1. Trees / binary tree
2. Binary tree / binary search tree
3. If BST do we have duplicates? And in which side?
4. Balanced (AVL tree) / unbalanced. Balanced doesn't mean having exact same size in left and right size. It means  "not terribly unbalanced" and ensures `O(log n)` for insert and find.

Types of binary trees:
1. Complete binary tree = every level of the tree is fully filled, except for perhaps the last level. Filled left to right.
2. Full binary tree = every node has either zero or two children.
3. Perfect binary tree = all leaf nodes at the same level, both full and complete. `len = 2^k - 1`, where `k` is depth of tree. 
4. Binary search tree = ordered binary tree. L < N <= R.

Notes on binary trees (page 102):
1. If TREE[0] = ROOT then
    - Left child of a node K => `2*K + 1`
    - Right child of a node K => `2*K + 2`
    - Parent of any node K => `floor(K/2) - 1`
2. Pre-order (NLR), post-order (LRN), in-order TRAVERSAL (LNR)
    - When we perform in-order traversal on BST, it visits the nodes in ascending order.
    - In pre-order the root is always visited first.
    - In post-order the root is always the last node visited.

Binary heaps (min-heap):
1. A min-heap is a complete binary tree where each node is smaller than its children. The root = min element in tree.
2. We have two methods, `insert()` and `extract_min()`, both `O(logn)`, where `n` is the number of nodes in the heap.

