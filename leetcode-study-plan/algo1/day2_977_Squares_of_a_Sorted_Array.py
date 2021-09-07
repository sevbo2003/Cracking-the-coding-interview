class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # first of all I  need to sort it kinda
        # then it is easier to make square

        squares = [i**2 for i in nums]
        print(">> squares", squares)

        # NOTE we need to have need to be serached only when there is at least one element in negative sign
        if nums[0] < 0:
            need_to_be_sorted = []
            for num in nums:
                if num < 0:
                    need_to_be_sorted.append(num)

            # need_to_be_sorted = [nums[i] for i in range(len(nums)-1) if nums[i] >= nums[i+1]]
            print(">> need_to_be_sorted", need_to_be_sorted)

            already_sorted = squares[len(need_to_be_sorted):]
            print(">> already_sorted", already_sorted)


            for i in range(len(need_to_be_sorted)):
                already_sorted.insert(self.insert(already_sorted, need_to_be_sorted[i]**2), need_to_be_sorted[i]**2)
                
            return already_sorted

        else:
            return squares

    def insert(self, nums, target):
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

            print(left)
            return left

# nums = [-4,-1,0,3,10]
nums = [-4,-4,-3]
sol = Solution()
print(sol.sortedSquares(nums))
