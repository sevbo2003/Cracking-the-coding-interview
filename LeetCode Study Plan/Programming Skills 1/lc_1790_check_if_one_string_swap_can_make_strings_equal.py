"""
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

SOLUTION:
    "bxankd"
    "kdanbx"
    Counter({'b': 1, 'x': 1, 'a': 1, 'n': 1, 'k': 1, 'd': 1})
    Counter({'k': 1, 'd': 1, 'a': 1, 'n': 1, 'b': 1, 'x': 1})

    "bank"
    "kanb"
    Counter({'b': 1, 'a': 1, 'n': 1, 'k': 1})
    Counter({'k': 1, 'a': 1, 'n': 1, 'b': 1})
"""
from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first_diff = -1
        second_diff = -1

        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                if first_diff == -1:
                    first_diff = idx
                elif second_diff == -1:
                    second_diff = idx
                else:
                    # found more than two differences
                    return False

        # if differences are equal in cross then strings would become equal
        return s1[first_diff] == s2[second_diff] and s1[second_diff] == s2[first_diff]

    def solution2(self, s1, s2):
        if s1 == s2:
            return True

        s1_counter = Counter(s1)  # We need counter because ["aa", "ac"] is wrong
        s2_counter = Counter(s2)

        print(s1_counter, s2_counter)

        if s1_counter == s2_counter:
            diff = 0
            for x, y in zip(s1, s2):
                if x != y:
                    diff += 1
                    if diff > 2:
                        return False
        else:
            return False

        return True
