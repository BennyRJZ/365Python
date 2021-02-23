# Given a non-empty array of integers nums, every element appears twice except for one. 
# Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without 
# using extra memory?
#EXAMPLE
# Input: nums = [2,2,1]
# Output: 1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        single = {}
        
        for num in nums:
            if num in single:
                single[num] += 1
            else:
                single[num] = 1
        
        
        for key, value in single.items():
            if value == 1:
                return key