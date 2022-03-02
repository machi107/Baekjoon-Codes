a,b=map(int,input().split())
r=[[]for i in range(b)]
z=[]
for i in range(a):
    t=list(map(int,input().split()))
    z.append(t[1])
    r[t[1]-1].append(t[0])
for i in range(b):r[i].sort()
for i in range(a):
    q=z[i]
    z[i]=r[z[i]-1][0]
    del r[q-1][0]
q=z.copy()
q.sort()
if z==q:print("Y")
else:print("N")
