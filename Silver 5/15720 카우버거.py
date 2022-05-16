a,b,c=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=list(map(int,input().split()))
q=sum(x)+sum(y)+sum(z)
x.sort()
y.sort()
z.sort()
t=0
for i in range(min(a,b,c)):t+=x[-1-i]+y[-1-i]+z[-1-i]
print(q)
print(q-t//10)
