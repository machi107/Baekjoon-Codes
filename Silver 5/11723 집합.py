import sys
z=sys.stdin.readline
a=int(z())
r=[0 for i in range(20)]
x=[1 for i in range(20)]
s=r.copy()
for _ in range(a):
    c=z().split()
    if c[0][:2]=="ad":s[int(c[1])-1]=1
    elif c[0][:2]=="re":s[int(c[1])-1]=0
    elif c[0][:2]=="ch":print(s[int(c[1])-1])
    elif c[0][:2]=="to":s[int(c[1])-1]=(s[int(c[1])-1]-1)%2
    elif c[0][:2]=="al":s=x.copy()
    else:s=r.copy()
