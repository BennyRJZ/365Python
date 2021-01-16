# Given two integers a and b, which can be positive or negative, find the 
# sum of all the integers between including them too and return it. If the
#  two numbers are equal return a or b.

# Note: a and b are not ordered!



def get_sum(a,b):
    
    if a == b:
        return a
    
    result = 0
    
    if a > b:
        for x in range(b,a+1):
            result = x + result
    elif a < b:
        for x in range(a,b+1):
            result = x + result
    return(result)
    
    
    #good luck!