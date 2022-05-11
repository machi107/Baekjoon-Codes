a,b=map(int,input().split())
c,x,z=int(input()),0,[]
d=list(map(int,input().split()))
for i in range(c):x+=a**i*d[-i-1]
while(x):z.append(x%b);x=x//b
z.reverse()
print(*z)
