import sys
st=sys.stdin.readline
a=int(st())
x,y=[],[]
for i in range(a):t=int(st());x.append(t);y.append(t)
y.sort(reverse=True)
for i in range(a):print(y.index(x[i])+1)
