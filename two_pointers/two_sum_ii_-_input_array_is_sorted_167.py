class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        What if we solve the problem with the help of target
        if the number we search is not in the dict we just put its subtraction
        """
        #         target_nums = {}
        #         for i in range(len(numbers)):
        #             if numbers[i] in target_nums:
        #                 return target_nums[numbers[i]] + 1, i + 1 # We need indexes
        #             else:
        #                 target_nums[target - numbers[i]] = i

        # Solution with two pointers
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1


