# Given a string, capitalize the letters that occupy even indexes and
#  odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. 
# See test cases for more examples.
# The input will be a lowercase string with no spaces.


def capitalize(s):
    sList = list(s)
    sList2 = list(s)
    result = []
    for i in range(0,len(s),2):
        sList[i]=sList[i].upper()
    r = ''.join([str(item) for item in sList]) 
    result.append(r)
    for i in range(1,len(s),2):
        sList2[i]=sList2[i].upper()
    r = ''.join([str(item) for item in sList2]) 
    result.append(r)
    print(result)
    return(result)