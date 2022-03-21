import sys

in_put = sys.stdin.readline

a= int(in_put())


d=list(map(int,in_put().split()))
if a<3:
    if a==2 and d[0] == d[1]:
        print (d[0])
    else:
        print("A")
else:      
    x=[]

    for i in range(1,a):
        x.append(d[i]-d[i-1])
    t=1
    if x[0]==0:
        q=0
    else:
        q=x[1]/x[0]
    
    for i in range(a-2):
        if x[i]!=0:
            if q  != x[i+1]/x[i]:
                t=0
                break
            q=x[i+1]/x[i]
            if q//1 != q:
                t=0
        else:
            if sum(x[i:])!=0:
                t=0
            

    plus=d[1]-(d[0]*q)
    d.append(d[a-1]*q+plus)
    if t:
        print(int(d[a]))
    else:
        print("B")

