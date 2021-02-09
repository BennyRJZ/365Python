# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
# that checks whether the two arrays have the "same" elements, with the same multiplicities
#  "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

import math  
def comp(array1, array2):
    if array2 == None or array1 == None:
        return False
    if len(array1) != len(array2):
        return False
    print(array1)
    print(array2)
    for x in array1:
        if x**2 in array2:
            num = array2.index(x**2)
            array2.pop(num)
        else:
            return False
    return True
	
    ### forma sencillaaaaa:
    # def comp(array1, array2):
    #     try:
    #     return sorted([i ** 2 for i in array1]) == sorted(array2)
    # except:
    #     return False