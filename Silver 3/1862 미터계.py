a=int(input())
p,t,n=a,10,1
o=t
while(t//o<a):
    z=a//t*n
    if a%t>=5*t/o:z+=n
    t*=o
    n*=9
    p-=z
print(p)
