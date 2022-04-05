a=int(input())
x=list(map(int,input().split()))
t=x[0]
for i in range(1,a):t=(t^x[i])
if t:print("koosaga")
else:print("cubelover")
