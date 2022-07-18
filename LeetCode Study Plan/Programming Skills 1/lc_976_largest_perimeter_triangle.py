from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        A = nums
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:  # Using the rules of triangles
                return A[i] + A[i+1] + A[i+2]
        return 0