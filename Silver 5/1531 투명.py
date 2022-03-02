a,b=map(int,input().split())
z=[[0 for i in range(100)] for h in range(100)]
for i in range(a):
    d,e,f,g=map(int,input().split())
    for x in range(d-1,f):
        for y in range(e-1,g):
            z[x][y]+=1
ans=0
for i in range(100):
    for j in range(100):
        if z[i][j]>b:ans+=1
print(ans)
