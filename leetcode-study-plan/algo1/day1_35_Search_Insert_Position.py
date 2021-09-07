class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
    

nums = [-1, 0, 3, 4, 9]
target = 3
sol = Solution()
print(sol.searchInsert(nums, target))