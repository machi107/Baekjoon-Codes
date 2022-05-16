a,b=map(int,input().split())
k=b//10
r=b%10
q=['000','001','002','010','011','100','020','021','110','030']
x,y,z=int(q[r][0]),int(q[r][1]),int(q[r][2])
x+=k*2
p=[]
t=a
for i in range(x):t*=1.35;t=int(t)
for i in range(y):t*=1.2;t=int(t)
for i in range(z):t*=1.05;t=int(t)
p.append(t)

t=a
for i in range(y):t*=1.2;t=int(t)
for i in range(x):t*=1.35;t=int(t)
for i in range(z):t*=1.05;t=int(t)
p.append(t)

t=a
for i in range(x):t*=1.35;t=int(t)
for i in range(z):t*=1.05;t=int(t)
for i in range(y):t*=1.2;t=int(t)
p.append(t)

t=a
for i in range(y):t*=1.2;t=int(t)
for i in range(z):t*=1.05;t=int(t)
for i in range(x):t*=1.35;t=int(t)
p.append(t)

t=a
for i in range(z):t*=1.05;t=int(t)
for i in range(x):t*=1.35;t=int(t)
for i in range(y):t*=1.2;t=int(t)
p.append(t)

t=a

for i in range(z):t*=1.05;t=int(t)
for i in range(y):t*=1.2;t=int(t)
for i in range(x):t*=1.35;t=int(t)

p.append(t)


print(max(p))
