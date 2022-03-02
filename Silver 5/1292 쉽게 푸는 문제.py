x=[]
i=1
while(len(x)<1000):
    for _ in range(i):
        x.append(i)
    i+=1
a,b=map(int,input().split())
print(sum(x[a-1:b]))
