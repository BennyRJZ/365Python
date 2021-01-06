# ##

# Given an array nums of integers, return how many of them contain an even number of digits.

# Example:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

##

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numb = ''
        numL = 0
        counter = 0
        for x in nums:
            numb = str(x)
            numL = len(numb)
            if (numL%2==0):
                print(x,numL)
                counter+=1
        
        return(counter)