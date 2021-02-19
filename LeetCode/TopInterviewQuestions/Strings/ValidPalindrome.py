# Given a string, determine if it is a palindrome, considering only alphanumeric characters
# and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            s="".join(c for c in s if c.isalpha() or c.isdigit())
            s=s.upper()
            print(s)
            print(s[::-1])
            if s==s[::-1]:
                return True
            else:
                return False