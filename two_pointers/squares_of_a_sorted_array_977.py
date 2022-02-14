class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = [], []
        for i in range(len(nums)):
            if nums[i] < 0:
                left.insert(0, -nums[i])
            if nums[i] >= 0:
                right.extend(nums[i:])
                break

        right_cur = 0
        for i in range(len(left)):
            while right_cur < len(right):
                if right[right_cur] >= left[i]:
                    right.insert(right_cur, left[i])
                    break
                right_cur += 1
            if right_cur == len(right):
                right.extend(left[i:])
                break

        return [x * x for x in right]