a=input()
pattern='o'
start=0
for i in range(a.count(pattern)):
    out=a.index(pattern,start)
    print(out)
    