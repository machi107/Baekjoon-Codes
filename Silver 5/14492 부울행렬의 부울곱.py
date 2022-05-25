x=[]
y=[]
a=int(input())
r=0
k=0
for i in range(a):x.append(list(map(int,input().split())))
for i in range(a):y.append(list(map(int,input().split())))
for i in range(a):
    for j in range(a):
        for m in range(a):k+=x[i][m]*y[m][j]
        if k:r+=1;k=0
print(r)
