class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            x = nums.pop()
            nums.insert(0, x)

        print(nums)


# nums = [1,2,3,4,5,6,7]
# k = 3

nums = [-1,-100,3,99]
k = 2

sol = Solution()
print(sol.rotate(nums, k))
        