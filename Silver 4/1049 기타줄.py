a,b=map(int,input().split())
z=r=1001
for _ in range(b):c,d=map(int,input().split());z=min(c,z);r=min(d,r);
print("%d"%min(a*r,z*(a//6)+min(a%6*r,z)))
