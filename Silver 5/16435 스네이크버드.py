a,b=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
for i in range(a):
    if b<c[i]:break
    b+=1
print(b)
