# Complete the method which accepts an array of integers, and returns one of the following:

# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise

def is_sorted_and_how(arr):
    sortedA = arr.copy()
    sortedD = arr.copy()
    
    sortedA.sort()
    print(arr)
    print(sortedA)
    
    sortedD.sort(reverse=True)
    print(arr,sortedD)
    
    if arr == sortedA:
        return('yes, ascending')
    elif arr == sortedD:
        return('yes, descending')
    else:
        return('no')
    
