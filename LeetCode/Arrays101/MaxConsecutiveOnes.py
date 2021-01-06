# #
# Given a binary array, find the maximum number of consecutive 1s in this array.

# #
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = 0
        result = 0
        count = 0
        for x in nums:
            if(x==0):
                count = 0
            else:
                count = count + 1
                result = max(result,count)
        return(result)

            