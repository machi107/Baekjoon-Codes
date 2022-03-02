a=int(input())
b=list(map(int,input().split()))
b.append(5500)
t,r,l=1,1,0
for i in range(a):
    if b[i]==b[i+1]:
        if l<r:l=r
        t,r=1,1
    elif t:
        if b[i]<b[i+1]:r+=1
        else:r+=1;t=0
    else:
        if b[i]>b[i+1]:r+=1
        else:
            if l<r:l=r
            t,r=1,2
if l<r:l=r-1
print(l)
