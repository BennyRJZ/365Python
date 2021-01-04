# Complete the solution so that it returns true if the first argument(string) passed in ends
#  with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(string, ending):
    strLen = len(string)
    endL = len(ending)
    
    stringCompare = string[-endL:]
    
    if ending == '':
        return True
    elif stringCompare == ending:
        return True
    else:
        return False