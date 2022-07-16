"""
LeetCode: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Problem: 1491. Average Salary Excluding the Minimum and Maximum Salary

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
             Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

SOLUTION 1:
    - Loop over list by finding max, and min elements
    - In the end subtract min and max
    - Time: O(n)
    - Space: O(1)

Constraints:
3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        sum_ = 0

        min_salary = float("inf")
        max_salary = float("-inf")

        for s in salary:
            sum_ += s

            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)

        result = (sum_ - min_salary - max_salary) / (len(salary) - 2)

        return result
