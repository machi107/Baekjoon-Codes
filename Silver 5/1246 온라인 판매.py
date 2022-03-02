a,b= map(int,input().split())
c=[]
for _ in range(b):
    c.append(int(input()))
c.sort()
d=[]
for i in range(b):
    d.append(c[i]*(min(a,b-i)))
t=max(d)
print(c[d.index(t)],t)
