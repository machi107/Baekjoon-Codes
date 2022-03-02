a,b=map(int,input().split())
x=[]
r=[0 for i in range(100000)]
for i in range(b):t=input().split();x.append([int(t[1]),t[0]]);r[int(t[1])]+=1
c=list(set(r))
c.sort()
c=c[1]
q=r.index(c)
for i in range(b):
    if x[i][0]==q:
        break
print(x[i][1],x[i][0])
