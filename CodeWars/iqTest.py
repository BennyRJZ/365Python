# Bob is preparing to pass IQ test. The most frequent task in this test
#  is to find out which one of the given numbers differs from the others.
#   Bob observed that one number usually differs from the others in evenness. 
#   Help Bob — to check his answers, he needs a program that among the given numbers
#    finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means
#  indexes of the elements start from 1 (not 0)




def iq_test(numbers):
    
    odd = 0
    even = 0
    
    x = [int(i) for i in numbers.split()]
    
    print(x)
    
    for a in x:
        if a%2 != 0:
            odd = odd + 1
        else:
            even = even + 1
    
    print(odd)
    print(even)
    
    number = 0
    
    if even > odd:
        for i in range(0,len(x)):
            if x[i]%2 != 0:
                number = i
                return number +1
    else:
        for i in range(0,len(x)):
            if x[i]%2 == 0:
                number = i
                return number + 1
            
            
        
    
    #your code here