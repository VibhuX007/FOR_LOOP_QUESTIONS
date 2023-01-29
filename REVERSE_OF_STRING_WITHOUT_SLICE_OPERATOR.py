#take input from user and print reverse of string without using slice operator.
a=input("enter the string")
b=len(a)
for i in range(b-1,-1,-1):
    print(a[i],end='')
    