# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python

def is_anagram(test, original):
    
    ### Check length
    
    if len(test) != len(original):
        return False
    
    ### Sort the word
    
    test = test.upper()
    original = original.upper()
    
    
    test = list(test)
    original = list(original)
    
    test.sort()
    original.sort()
    
    for i in range(0,len(original)):
        if test[i] != original[i]:
            return False
    
    
    return True