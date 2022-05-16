import itertools
a,b=map(int,input().split())
t=list(map(int,input().split()))
t.sort()
l=len(str(a))
q=str(t[0])*l
if a<int(q):print(str(t[-1])*(l-1))
else:
    p=0
    k=list(itertools.product(t,repeat=l))
    for i in range(len(t)**l):
        u=""
        for j in range(l):
            u+=str(k[i][j])
        x=int(u)
        if x>p and x<=a:p=x
    


    print(p)
