# Your goal in this kata is to implement a difference function, 
# which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]

#link  https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    if len(a) == 0:
        return a
    elif len(b) == 0:
        return a
    for i in b:
        value = i
        aux = a
        a = []
        for x in aux:
            if x != value:
                a.append(x)
        print(a)
                
    
    return(a)
    # correcion