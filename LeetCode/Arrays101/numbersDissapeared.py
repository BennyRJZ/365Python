# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
# some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? 
# You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if len(nums)<=0:
            return []
        
        check = []
        a = 1
        z = len(nums)
        
        check = range(a,z+1)
        check = set(check)
        
#         result = []
#         for x in check:
#             if x not in nums:
#                 result.append(x)
#             else:
#                 continue
        
#         return(result)

        result = check - set(nums)
        return(list(result))
    
    ### We created 2 sets, one with the sequence of numbers and another with the original array
    ### the result its the substraction of the checkList - the original list