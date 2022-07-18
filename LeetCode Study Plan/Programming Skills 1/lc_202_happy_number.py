"""
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        unique_sq_nums = set()

        while True:
            sq_num = sum(int(i) ** 2 for i in str(n))

            if sq_num == 1:
                return True
            if sq_num in unique_sq_nums:
                return False

            unique_sq_nums.add(sq_num)
            n = sq_num
