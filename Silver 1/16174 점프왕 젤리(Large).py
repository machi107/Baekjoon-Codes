x=[]
a=int(input())
z=[[0 for i in range(a)] for _ in range(a)]
for i in range(a):x.append(list(map(int,input().split())))
z[0][0]=1
z[a-1][a-1]=-1

for i in range(a):
    for j in range(a):
        k=x[i][j]
        if z[i][j]>0:
            if i+k<a:z[i+k][j]+=1
            if j+k<a:z[i][j+k]+=1
if z[a-1][a-1]==-1:print("Hing")
else:print("HaruHaru")
