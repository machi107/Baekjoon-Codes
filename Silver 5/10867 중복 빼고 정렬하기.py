input()
x=list(set(map(int,input().split())))
x.sort()
r=""
for i in x:r+=str(i)+" "
print(r[:-1])
