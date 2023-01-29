#TAKE INPUT FROM USER AND PRINT REVERSE OF WORDS. FOR EXAMPLE- HOW ARE YOU = YOU ARE HOW
'''
a=input()
y=a.split()
for i in range(len(y)-1,-1,-1):
    print(y[i],end="")
'''
x=input()
y=x.split()
c=y[::1]
d=" ".join(c)
print(d)