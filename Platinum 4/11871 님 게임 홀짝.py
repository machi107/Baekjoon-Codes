a=int(input())
x=list(map(int,input().split()))
for i in range(a):
    if x[i]%2:x[i]=(x[i]+1)//2
    else:x[i]=(x[i]-2)//2
t=x[0]
for i in range(1,a):t=(t^x[i])
if t:print("koosaga")
else:print("cubelover")
