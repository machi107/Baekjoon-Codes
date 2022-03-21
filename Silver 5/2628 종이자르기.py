a,b=map(int,input().split())
x=[0,a]
y=[0,b]
for i in range(int(input())):
    c,d=map(int,input().split())
    if c:x.append(d)
    else:y.append(d)
x.sort()
y.sort()
w=0
z=0
for i in range(len(x)-1):
   r=x[i+1]-x[i]
   if r>w:w=r
for i in range(len(y)-1):
   r=y[i+1]-y[i]
   if r>z:z=r
print(w*z)
