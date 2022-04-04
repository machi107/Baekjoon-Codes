z=int(input())
for i in range(z):
    a,b=map(int,input().split())
    f=[]
    for h in range(a):
        f.append(input())
    c,d=map(int,input().split())
    q=[]
    for h in range(c):
        q.append(input())
    ans=0
    
    for j in range(c-a+1):
        for h in range(d-b+1):
            br=0
            if q[j][h] == f[0][0]:
                ans+=1
                for ii in range(a):
                    for jj in range(b):
                        if q[j+ii][h+jj] != f[ii][jj]:
                            br=1
                    if br:
                        ans-=1
                        break

    print(ans)
