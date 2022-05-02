a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[]
r=0
for i in range(9):r+=a[i];x.append(r);r-=b[i];x.append(r)
q=0
for i in range(18):
    if x[i]>0:q=1;break;
if q and x[17]<0:print("Yes")
else:print("No")
