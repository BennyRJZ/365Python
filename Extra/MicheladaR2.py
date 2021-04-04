#Order the letters in alphabetical order 

def orderL(string):
    orderedList = sorted(string)
    string = "".join(orderedList)
    print(string)


case1 = "Benny"
case2 = "Ruiz"
case3 = "Jimenez"

orderL(case1)
orderL(case2)
orderL(case3)