#DEFINE A FUNCTION TO PRINT A FIBONACCI SERIES?
def fab(v):
    a=b=0
    c=1
    for i in range(0,v):
        print(b)
        a=b+c
        b=c
        c=a

v = int(input('Enter the number '))
fab(v)
