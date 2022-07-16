class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s = s[::-1]

        length = len(s) # 5
        for i in range(length // 2):
            s[i], s[length-i-1] = s[length-i-1], s[i]


        return s
        
s = ["h","e","l","l","o"]

sol = Solution()

print(sol.reverseString(s))
