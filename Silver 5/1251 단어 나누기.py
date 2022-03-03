a=input()
t=len(a)
x=[]
r=[]
for i in range(1,t-1):
    for j in range(i+1,t):
        x.append([i,j])
        q=a[:i]
        w=a[i:j]
        e=a[j:]
        r.append(q[::-1]+w[::-1]+e[::-1])
r.sort()
print(r[0])
