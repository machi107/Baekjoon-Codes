a,b=map(int,input().split())
x=y={}
for i in range(a):z=input();x[z],y[i]=i,z
for _ in range(b):t=input();print(y.get(int(t)-1))if t[0].isdigit()else print(x.get(t)+1)
