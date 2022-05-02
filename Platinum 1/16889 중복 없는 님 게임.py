q,t,a,r=[1],2,int(input()),0
while(q[-1]<60):q.append(q[-1]+t);t+=1
x=list(map(int,input().split()))
for i in range(a):
    for j in range(11):
        if x[i]<q[j]:break
    r^=j
print("koosaga") if r else print("cubelover")
