"""
https://leetcode.com/problems/reshape-the-matrix/

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]) or (r == len(mat) and c == len(mat[0])):
            return mat

        # else I need to transform the matrix
        flatted_mat = []
        for i in mat:
            flatted_mat += i

        result = []
        for row in range(r):  # row
            result.append(flatted_mat[row*c: row*c+c])

        return result
