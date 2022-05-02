z,n,c=map(int,input().split())
m=1
while(n):
    if n%2:m*=z
    z*=z
    z=z%c
    n=n//2
print(m%c)
