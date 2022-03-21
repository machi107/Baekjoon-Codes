d=[0 for _ in range(200)]
t=[0 for _ in range(200)]
a,b=map(int,input().split())
for _ in range(a+b):e,f=map(int,input().split());d[e]=f;t[e]=100
x=[1]
y=[]
ans=1
while(t[100]==0):
    while(len(x)):
        for i in range(1,7):
            if t[x[0]+i]==100:
                t[d[x[0]+i]]=ans
                y.append(d[x[0]+i])
            if not t[x[0]+i]:
                t[x[0]+i]=ans
                y.append(x[0]+i)
        del x[0]
    ans+=1
    while(len(y)):
        for i in range(1,7):
            if t[y[0]+i]==100:
                t[d[y[0]+i]]=ans
                x.append(d[y[0]+i])
            if not t[y[0]+i]:
                t[y[0]+i]=ans
                x.append(y[0]+i)
        del y[0]
    ans+=1
print(t[100])
