"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Problem: Merge all overlapping intervals

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
[[1,4],[0,4]] for this reason we need to sort
[[1,4],[2,3]] for this reason we need to save max
"""


def merge(intervals: List[List[int]]) -> List[List[int]]:

    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x[0])

    arr = intervals
    i = 0
    while i < len(intervals) - 1:
        if arr[i][1] >= arr[i + 1][0]:
            arr[i][1] = max(arr[i + 1][1], arr[i][1])
            arr.pop(i + 1)
        else:
            i += 1

    return intervals
