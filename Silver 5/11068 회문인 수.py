a=int(input())
for i in range(a):
    u=0
    b=int(input())
    for k in range(2,65):
        c=b
        x=[]
        while(c):
            x.append(c%k)
            c=c//k
        z=1
        for t in range(len(x)):
            if x[t]!=x[-t-1]:z=0
        if z:
            u=1
            break;
    print(u)
