while(1):
    r="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    x=list(map(int,input().split()))
    if sum(x)==0:break
    x=x[1:]
    ans=0
    t=[0 for i in range(500)]
    for i in range(20):
        if t[i]==0:
            t[i]=r[0];r=r[1:]
        

        if t[i+x[i%len(x)]]==0 or i+x[i%len(x)]>20:
            t[i+x[i%len(x)]]=t[i]
        else:ans="CRASH"
    if ans:print(ans)
    else:
        rr=""
        for i in range(20):
            rr+=t[i]
        print(rr)

    
