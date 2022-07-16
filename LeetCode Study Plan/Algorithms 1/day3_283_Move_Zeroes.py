class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        for i in range(len(nums)):
            if nums[counter] == 0:
                nums.append(0)
                nums.pop(counter)
                print('*')
            else:
                counter += 1

        # last_non_zero = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
        #         last_non_zero += 1

nums = [0,1,0,3,12]

sol = Solution()
print(sol.moveZeroes(nums))