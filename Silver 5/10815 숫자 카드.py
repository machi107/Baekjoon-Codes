a=int(input())
x=list(map(int,input().split()))
b=int(input())
y=list(map(int,input().split()))
x.sort()
t=[]
for i in y:
    q=0
    r=a-1
    while(1):
        if x[r]==i or x[q]==i:
            t.append(1)
            break
        elif r-q==1:
            t.append(0)
            break
        elif x[(q+r)//2]>=i:
            r=(q+r)//2
        elif x[(q+r)//2]<i:
            q=(q+r)//2
print(*t)
