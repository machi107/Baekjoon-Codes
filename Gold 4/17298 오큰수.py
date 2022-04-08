a=int(input())
b=list(map(int,input().split()))
z=[-1]*a
s=[]
s.append(0)
for i in range(1,a):
    while s and b[s[-1]]<b[i]:
        z[s.pop()]=b[i]
    s.append(i)
print(*z)
