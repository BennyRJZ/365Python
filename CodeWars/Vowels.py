# Your task is to write a function that takes a string and return a new string with 
# all vowels removed.

# For example, the string 
# "This website is for losers LOL!" would become 
# "Ths wbst s fr lsrs LL!".

#link https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']    
    
    for item in vowels:
        string = string.replace(item,'')
        
    
    return(string)


