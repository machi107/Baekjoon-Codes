a,b,c=map(int,input().split())
x=""
t=[]
for i in range(b):t.append(list(input()))
for i in range(b-1):
    for j in range(a*c):
        if t[i][j]!="?":t[i+1][j]=t[i][j]
for i in range(a):
    q=(t[-1][i*c:i*c+c])
    z=list(set(q))
    z.sort()
    x+=(z[-1])
print(x)
