# Your task is to write a function which returns the sum of following series upto nth term(parameter).

# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...


# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

def series_sum(n):
    
    
    n=n*3
    
    res = 0
    
    
    for x in range(1,n,3):
        res = res + 1/x
        
    res = format(res,'.2f')
    strR = str(res)
    
    
    return(strR)
    
