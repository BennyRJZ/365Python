# Create the function prefill that returns an array of n elements that all 
# have the same value v. See if you can do this without using a loop.

# You have to validate input:

# v can be anything (primitive or otherwise)
# if v is ommited, fill the array with undefined
# if n is 0, return an empty array
# if n is anything other than an integer or integer-formatted string 
# (e.g. '123') that is >=0, throw a TypeError
# When throwing a TypeError, the message should be n is invalid, 
# where you replace n for the actual value passed to the function.

# Code Examples

def prefill(n,v):
    
    if type(v) is str:
         raise TypeError("STR")
    
    elif n is None:
        raise TypeError("None is invalid")
    
    elif n <0:
        raise TypeError("NUM MENOR")
        
    elif n == int(n):
        if n == 0:
            return []
    
        arr = []    
        for i in range(0,n):
            arr.append(v)
        
        return(arr)
        #your code here
    else:
        raise TypeError(n + " is invalid")