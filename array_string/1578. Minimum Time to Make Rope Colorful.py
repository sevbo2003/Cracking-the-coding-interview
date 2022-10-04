"""
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

Problem: Minimum time to remove the adjacent similar items, and only 1 item should be left.

Solution:
    1. Find continuous substring of similar chars
    2. THe compare the needed time and take only minimum so that 1 element left
HOW?
    1. Save the start INDEX and CHAR, compare with adjacent elements if similar then increase COUNTER.
       If not similar and counter > 0 then take all mina and slice using INDEX and COUNTER, and add to COST.

"""


def minCost(colors: str, neededTime: list[int]) -> int:
    colors = ''.join([colors, '0'])  # TODO: because the loop doesn't count the last element

    def calculated_mins(array: list):
        # [2,3,1,3,5]
        return sum(array) - max(array)  # TODO

    cost = 0
    index = 0
    counter = 0
    char = colors[0]

    for i in range(1, len(colors)):
        if colors[i] == char:
            counter += 1
        elif colors[i] != char and counter > 0:
            slice_ = neededTime[index:index + counter + 1]
            mins = calculated_mins(slice_)
            cost += mins
            counter = 0

        if counter == 0:
            char = colors[i]
            index = i

    return cost


# colors = "abaac"
# neededTime = [1, 2, 3, 4, 5]

colors = "aabaa"
neededTime = [1,2,3,4,1]

result = minCost(colors, neededTime)
pass
