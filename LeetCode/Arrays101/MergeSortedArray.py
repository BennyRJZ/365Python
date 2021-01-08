# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively.
#  You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements
#  from nums2.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]


### https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        sortedArray = []
        
#         for i in range(m,len(nums1)):
#             nums1.pop()
        
#         for j in range(0,n):
#             nums1.append(nums2[j])
            
#         nums1.sort()

#Optimal
        x = 0
        for i in range(m,m+n):
            nums1[i] = nums2[x]
            x = x + 1
        
        nums1.sort()