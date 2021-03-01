# The included code stub will read an integer,
# from STDIN.

# Without using any string methods, 
# try to print the following:
# 123..n
if __name__ == '__main__':
    n = int(input())
    
    numbers = list(range(1,n+1))
    
    str1 = ""
    for number in numbers:
        str1 = str1+str(number)
    print(str1)