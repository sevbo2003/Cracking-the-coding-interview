# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n

        for i in range(n, -1, -1):
            mid = (left + right) // 2
            
            if isBadVersion(mid) == True:                
                if isBadVersion(mid-1) == False:
                    return mid
                else: # meaning that it is true then 
                    right = mid - 1 
                     
            elif isBadVersion(mid) == False:
                left = mid + 1
        