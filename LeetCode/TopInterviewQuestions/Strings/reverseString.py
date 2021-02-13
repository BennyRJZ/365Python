
# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place
#  with O(1) extra memory.

# # You may assume all the characters consist of printable ascii characters.

# 1st way:  using python methods
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         s.reverse()
#         print(s)

# 2nd way iterating the list.
class Solution:
    def reverseString(self, s: List[str]) -> None:
        counter = -1 #pointing to last item on the list
        pivot = ""
        for i in range(0,len(s)/2):
            pivot = s[i]
            s[i] = s[counter]
            s[counter] = pivot
            counter = counter-1
#         s.reverse()
#         print(s)

