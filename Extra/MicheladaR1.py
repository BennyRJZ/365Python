##Count the number of words in a string, the words are separated by " "

def numberWord(string):
    print(len(string.split()))

case1 = "Hi my name is Benny"
case2 = "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression."


numberWord(case1)
numberWord(case2)
