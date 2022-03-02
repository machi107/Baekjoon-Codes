a,t,x=int(input()),0,[]
for i in range(a):x.append(int(input()))
while(max(x)!=x[0]):x[x.index(max(x))]-=1;x[0]+=1;t+=1
if x.count(x[0])>1:t+=1
print(t)
