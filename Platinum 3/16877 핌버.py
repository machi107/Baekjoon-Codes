x=[1,2]
while(x[-1]+x[-2]<3000001):x.append(x[-1]+x[-2])
t=[0 for i in range(3000001)]
t[0]=0
for i in range(1,3000001):
    r=[]
    for j in range(len(x)):
        if i<x[j]:break
        else:r.append(t[i-x[j]])
    for j in range(len(r)+1):
        if not j in r:t[i]=j;break
a=int(input())
z=0
q=list(map(int,input().split()))
for i in q:z^=t[i]
if z:print("koosaga")
else:print("cubelover")
