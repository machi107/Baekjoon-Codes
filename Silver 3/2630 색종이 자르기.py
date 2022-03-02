import sys
in_put = sys.stdin.readline

a=int(in_put())
ans=[0,0]

b=[]

for _ in range(a):
    b.append(list(map(int,in_put().split())))

def pan(x,n):
    t=0
    for i in range(n):
        t+=sum(x[i])
    if n!=1:
        if t==n*n:
            ans[0]+=1
        elif t==0:
            ans[1]+=1
        else:
            c=[x[i][:n//2] for i in range(n//2)]
            pan(c,n//2)
            d=[x[i][n//2:] for i in range(n//2)]
            pan(d,n//2)
            e=[x[n//2+i][:n//2] for i in range(n//2)]
            pan(e,n//2)
            f=[x[n//2+i][n//2:] for i in range(n//2)]
            pan(f,n//2)

    else:
        if sum(x[i]):
            ans[0]+=1
        else:
            ans[1]+=1
    
pan(b,a)

print(ans[1],ans[0],sep="\n")


