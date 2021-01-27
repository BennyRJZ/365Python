# Given an array (arr) as an argument complete the function countSmileys that 
# should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]


def count_smileys(arr):
    number = 0
    
    happy = [")","D"]
    nose = ["-","~"]
    eyes = [":",";"]
    
    print(arr)
    for x in arr:
        if len(x) == 3:
            if x[2] in happy and x[1] in nose and x[0] in eyes:
                number = number + 1
        elif len(x) == 2:
            if x[1] in happy and x[0] in eyes:
                number = number + 1
        else:
            continue
    
    return number