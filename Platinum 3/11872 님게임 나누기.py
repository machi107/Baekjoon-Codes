a=int(input())
x=list(map(int,input().split()))
for i in range(a):
    if x[i]%4==0:x[i]-=1
    elif x[i]%4==3:x[i]+=1
t=x[0]
for i in range(1,a):t=(t^x[i])
if t :print("koosaga")
else:print("cubelover")
