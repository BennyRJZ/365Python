# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
#  then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        if x>=-2**31 and x<=2**31-1:
            negative = False
        
            if x<0:
                negative = True
                x = x * -1

            xs = (str(x)[::-1])
            x = int(xs)

            if negative == True:
                return (x*-1)
            else:
                return x
        
        else:
            return 0

        