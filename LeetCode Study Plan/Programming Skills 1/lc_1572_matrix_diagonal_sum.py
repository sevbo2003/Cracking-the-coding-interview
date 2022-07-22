"""
https://leetcode.com/problems/matrix-diagonal-sum/

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_ = 0
        size = len(mat)
        for i in range(size):
            sum_ += mat[i][i] + mat[i][size - i - 1]

        if size % 2:
            sum_ -= mat[size // 2][size // 2]

        return sum_
