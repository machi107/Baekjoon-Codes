a=int(input())
x=[]
for i in range(a):
    x.append(list(map(int,input().split())))
p=[]
for i in range(a):
    q=[]
    for j in range(a):
        q.append((x[i][0]-x[j][0])**2+(x[i][1]-x[j][1])**2)
    p.append(max(q))
z=p.index(min(p))
print(x[z][0],x[z][1])
