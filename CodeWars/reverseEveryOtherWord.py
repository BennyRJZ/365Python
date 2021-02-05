# Reverse every other word in a given string, then return the string.
#  Throw away any leading or trailing whitespace, while ensuring there is exactly one space between 
#  each word. Punctuation marks should be treated as if they are a part of the word in this kata.

def reverse_alternate(string):
    strList = string.split()
    counter = 0
    result = []
    for x in strList:
        if counter%2 == 0:
            result.append(x)
        else:
            txt = x[::-1]
            result.append(txt)
        counter = counter + 1
    
    listToStr = ' '.join(map(str, result)) 
    return(str(listToStr))  
        
    
        