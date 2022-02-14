"""


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


"""

counter = 0

for _ in range(len(nums)):

    if nums[counter] == 0:
        # append, pop(counter)
        nums.append(0)
        nums.pop(counter)
    else:
        counter += 1


