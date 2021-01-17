# Given a fixed length array arr of integers, duplicate each occurrence of zero,
#  shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written.

# Do the above modifications to the input array in place, do not return anything from your function.


class Solution(object):
    def duplicateZeros(self, arr):
        
        dupZ = []
        
        for x in arr:
            if x == 0:
                dupZ.append(x)
            dupZ.append(x)
        
        for i in range(0,len(arr)):
            arr[i] = dupZ[i]
        
        
        print(arr)
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        