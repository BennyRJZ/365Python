# Given an array arr of integers, check if there exists two integers N
#  and M such that N is the double of M ( i.e. N = 2 * M).

# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# link  https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]*2 in arr and arr.index(arr[i]*2) != i:  ### check if the index it's different
                return True                                    ### if a 0 appears
        