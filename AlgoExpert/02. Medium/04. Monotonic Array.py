# O(N) time | O(1) space
def solution1(nums: list) -> bool:
    def breaks_direction(direction, prev, curr) -> bool:
        ...

    if len(nums) <= 2:
        return True

    direction = nums[1] - nums[0]
    for i in range(2, len(nums)):
        if direction == 0:  # Meaning the same numbers
            direction = nums[i] - nums[i-1]
            continue
        if breaks_direction(direction, nums[i-1], nums[i]):
            return False

    return True


# O(N) time | O(1) space
def solution2(nums: list) -> bool:
    A = nums
    increasing = decreasing = True

    for i in range(len(A) - 1):
        if A[i] > A[i+1]:
            increasing = False
        if A[i] < A[i+1]:
            decreasing = False

    return increasing or decreasing
