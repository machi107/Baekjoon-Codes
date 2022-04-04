a=int(input())
for i in range(a):
    x=list(map(int,input().split()))
    x=x[1:]
    x.sort()
    t=0
    for k in range(1,len(x)):
        q=x[k]-x[k-1]
        if q>=t:t=q;
    print("Class ",i+1,"\nMax ",max(x),", Min ",min(x),", Largest gap ",t,sep="")
