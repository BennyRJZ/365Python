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
    #your code here