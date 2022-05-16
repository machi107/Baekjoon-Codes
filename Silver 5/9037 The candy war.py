for i in range(int(input())):
    k=int(input())
    x=list(map(int,input().split()))
    q=0
    for j in range(k):
        if x[j]%2:x[j]+=1

    while(x.count(x[0])!=k):
        q+=1

        p=[0 for i in range(k)]
        for j in range(k):p[j]+=x[j]//2;x[j]/=2
        t=p[0]
        p=p[1:]
        p.append(t)
        for j in range(k):x[j]+=p[j]
        for j in range(k):
            if x[j]%2:x[j]+=1
    print(q)
