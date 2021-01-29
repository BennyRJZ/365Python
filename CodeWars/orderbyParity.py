
def sortArrayByParity(self, A: List[int]) -> List[int]:
    aux = []
    
    for x in A[:]:
        if (x%2)!=0:
            print(x)
            aux.append(x)
            A.remove(x)
    for y in aux:
        A.append(y)
    
    print(aux)
    return(A)