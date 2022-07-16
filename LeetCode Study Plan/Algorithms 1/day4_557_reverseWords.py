class Solution:
    def reverseWords(self, s: str) -> str:
        
        # s = s.split()

        # for i in range(len(s)):
        #     s[i] = s[i][::-1]
            
        # return ' '.join(s)


        s = list(s)
        length = len(s) # 5
        for i in range(length // 2):
            s[i], s[length-i-1] = s[length-i-1], s[i]


        return s

            
        
s = "Let's take LeetCode contest"

sol = Solution()

print(sol.reverseWords(s))