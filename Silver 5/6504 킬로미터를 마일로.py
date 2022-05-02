x=[1,2]
while(x[-2]+x[-1]<25001):x.append(x[-2]+x[-1])
a=int(input())
for i in range(a):
    t=int(input())
    r=0
    for j in range(len(x)-1):
        if t>=x[-j-1]:t-=x[-j-1];r+=x[-j-2]
    print(r)
