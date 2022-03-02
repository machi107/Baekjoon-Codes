a,b=map(int,input().split())
c=[]
d=[]
for i in range(a):c.append(input())
for i in range(b):d.append(input())
z=list(set(c) & set(d))
z.sort()
print(len(z))
for i in z:print(i)
