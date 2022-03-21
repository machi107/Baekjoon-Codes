a=int(input())
t=0
if a<100:
    for i in range(1,a+1):
        x=[a]
        x.append(i)
        while(x[-1]>=0):
            x.append(x[-2]-x[-1])
        if len(x)-1>t:
            t=len(x)-1
            q=x.copy()
else:
    c=a//100*50
    e=a//100*75
    for i in range(c-1,e):
        x=[a]
        x.append(i)
        while(x[-1]>=0):
            x.append(x[-2]-x[-1])
        if len(x)-1>t:
            t=len(x)-1
            q=x.copy()
print(t)
for i in range(t):
    if i!=t-1:
        print(q[i],end=" ")
    else:print(q[i])
