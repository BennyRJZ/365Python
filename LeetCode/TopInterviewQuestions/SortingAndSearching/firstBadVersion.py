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
        
        i = 0
        j = n
        piv = 0
        ###### BINARY SEARCH
        while i<=j:
            
            piv = i + (j-i)//2
            
            if isBadVersion(piv) == False:
                i = piv + 1
            else:
                j = piv -1
        
        if isBadVersion(piv) == False:
            return piv +1
        else:
            return piv
        
            