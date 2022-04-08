a,b=map(int,input().split())
r=[]
for i in range(a):
    x=list(map(int,input().split()))
    r.append(sum(x))
t=r[0]
for i in range(1,a):t=(t^r[i])
if t:print("august14")
else:print("ainta")
