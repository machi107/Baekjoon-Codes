a,b=map(int,input().split())
r,t=a+b-1,1
for i in range(1,b):t*=(r-i+1)
for i in range(1,b):t//=i
print(t%(10**9))
