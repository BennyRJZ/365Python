# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters
#  and your task is to convert that string to either lowercase only or uppercase only based on:
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, 
# convert the string to lowercase.

# link : https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python


def solve(s):
    
    sl = list(s)
    print(sl)
    
    countU = 0
    countL = 0
    
    for x in sl:
        if x.islower():
            countL = countL +1
        elif x.islower() != True:
            countU = countU +1
        else: continue
    
    if countL > countU:
        s = s.lower()
    elif countL < countU:
        s = s.upper()
    else:
        s = s.lower()
    
    return s