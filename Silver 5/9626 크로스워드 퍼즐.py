a,b=map(int,input().split())
c,d,e,f=map(int,input().split())
p="#."*20
r=b+d+e
for i in range(a+c+f):
    t=i%2
    if i<c or i>=c+a:print(p[t:r+t])
    else:print(p[t:d+t]+input()+p[b+d+t:r+t])
