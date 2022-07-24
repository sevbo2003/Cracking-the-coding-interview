"""
https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # v2: Mathematical approach
        sum_ = 0
        len_ = len(arr)
        for i in range(len_):
            sum_ += (((i + 1) * (len_ - i) + 1) // 2) * arr[i]
        return sum_

    def v1(self, arr: List[int]) -> int:
        sum_ = 0
        len_ = len(arr)
        border = len_ if len_ % 2 else len_ - 1
        slice_ = 1

        while slice_ <= border:
            i = 0
            while i < len_:
                upper_bound = i + slice_
                if upper_bound <= len_:
                    sum_ += sum(arr[i:upper_bound])
                i += 1

            slice_ += 2

        return sum_
