"""
LeetCode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Problem: Given the string and k, remove k occurrences of the adjacent characters
"""


def removeDuplicates(s: str, k: int) -> str:
    is_last_deleted = True

    while is_last_deleted:
        char = s[0]
        counter = 1  # K tracker
        i = 1
        while i < len(s):
            if s[i] == char:
                counter += 1
                if counter == k:
                    # change string deeedbbcccbdaa
                    s = "".join([s[:i - k + 1], s[i + 1:]])
                    i -= k
                    break
            else:
                # start = i
                char = s[i]
                counter = 1

            if i == len(s) - 1:
                is_last_deleted = False

            i += 1

    return s


if __name__ == '__main__':
    s = "deeedbbcccbdaa"
    k = 3
    print(removeDuplicates(s, k))
