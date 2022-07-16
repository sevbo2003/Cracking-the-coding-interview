"""
LeetCode: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

Problem: Given two non-negative integers low and high.
         Return the count of odd numbers between low and high (inclusive).

Input: low = 3, high = 7
Output: 3

SOLUTION 1: #BAD
    - Loop in range and check if the element is even or odd and increment the counter
    - Time: O(high-low)
    - Space: O(1)

SOLUTION 2:
    - Use simple formula (high - low) // 2
    - Inclusive numbers should be also included so
        - Check if any number is odd and add 1
    - Time: O(1)
    - Space: O(1)
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high % 2 or low % 2:
            checker = 1
        else:
            checker = 0
        return (high - low) // 2 + checker
