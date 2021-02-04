# It's time to create an autocomplete function! Yay!

# The autocomplete function will take in an input string and a dictionary array 
# and return the values from the dictionary that start with the input string.
#  If there are more than 5 matches, restrict your output to the first 5 results.
#   If there are no matches, return an empty array.
import re
def autocomplete(input_, dictionary):
    cleanString = re.sub('\W+','', input_ )
    alphanumeric = [character for character in cleanString if character.isalnum()]
    alphanumeric = "".join(alphanumeric)
    
    only_alpha = ""
    for char in cleanString:
        if char.isalpha():
            only_alpha += char
    
    cap = only_alpha.capitalize()
    matches = []
    print("----")
    print(input_)
    print(dictionary)
    print("----")
    for i in range(0,len(dictionary)):
        if dictionary[i].startswith(only_alpha) or dictionary[i].startswith(cap):
            print(only_alpha)
            print(dictionary[i])
            matches.append(dictionary[i])
        else:
            continue
    print(matches[0:5])
    return(matches[0:5])