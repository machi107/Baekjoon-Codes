a,b=map(int,input().split())
x=list(list(map(int,input().split())))
t=[]
for i in range(a-b+1):
    q=0
    for j in range(b):
        q+=x[i+j]
    t.append(q)
print(max(t))
