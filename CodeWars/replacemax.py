# Given an array arr, replace every element in that array with the greatest element
#  among the elements to its right, and replace the last element with -1.

# After doing so, return the array.



class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(0,len(arr)-1):
            m = max(arr[i+1::])
            idx = arr.index(m)
            arr[i] = m
        x= len(arr)-1
        arr[x] = -1
        return(arr)