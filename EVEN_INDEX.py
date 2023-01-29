#python program to get string from user and print characters of even index without using slice operator.
x=str(input("enter the string"))
for i in range (0,len(x)):
    if(i%2==0):
        print(x[i])