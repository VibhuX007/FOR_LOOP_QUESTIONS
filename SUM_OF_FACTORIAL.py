n = int(input("enter a number:"))
s = 0
for i in range(1,n+1):
    f = 1
    for j in range(2,i+1):
        f*=j
    s += 1/f
    n //= 10
print(s)