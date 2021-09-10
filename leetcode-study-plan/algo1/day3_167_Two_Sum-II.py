class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        possible_nums = {}
        
        for i in range(len(nums)):
            if nums[i] in possible_nums:
                print(">> poss", possible_nums)
                return possible_nums[nums[i]] + 1, i + 1 
            else:    
                possible_nums[target-nums[i]] = i  
            



# numbers = [2,7,11,15] 
# target = 9

numbers = [2,3,4]
target = 6

sol = Solution()
print(sol.twoSum(numbers, target))