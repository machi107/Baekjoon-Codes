a,b=map(int,input().split())
r=int(input())
k=1
z=0
for i in range(1,a):
    p=int(input())
    if k and r<p:z+=b//r;b%=r;k-=1;
    if k==0 and r>p:b+=z*r;z=0;k+=1
    r=p
if z:b+=z*r
print(b)
