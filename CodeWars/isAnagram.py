# What is an anagram? Well, two words are anagrams of each other if they both contain the same 
# letters. For example:

# 'abba' & 'baab' == true

# 'abba' & 'bbaa' == true

# 'abba' & 'abbba' == false

# 'abba' & 'abca' == false

def anagrams(word, words):
    word = "".join(sorted(word))
    print(word)
    
    aux = ""
    result=[]
    for x in words:
        aux = "".join(sorted(x))
        if aux == word:
            result.append(str(x))
    return(result)
        