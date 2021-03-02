# Given a string, find the first non-repeating character in it and return its index.
#  If it doesn't exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        
        for char in s:
            if char in unique:
                unique[char] += 1
            else:
                unique[char] = 1
        
        uniqchar = -1
        for key, value in unique.items():
            if value == 1:
                uniqchar = key
                break
                
        for i in range(0,len(s)):
            if s[i] == uniqchar:
                print(i)
                return(i)
                
            else:
                return uniqchar
        