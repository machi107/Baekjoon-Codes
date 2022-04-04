import itertools
a,b=map(int,input().split())
x=set(input().split())
r={'a','e','i','o','u'}
q=[]
z=list(itertools.combinations(x,a))
for i in range(len(z)):
    z[i]=set(z[i])
    if a-len(z[i]&r)>1 and len(z[i]&r):
        t=""
        z[i]=list(z[i])
        z[i].sort()
        for j in range(a):
            t+=z[i][j]
        q.append(t)
q.sort()
for i in range(len(q)):
    print(q[i])
