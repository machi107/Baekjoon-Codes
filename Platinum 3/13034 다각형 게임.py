a=[0,1,1]
n=int(input())
for i in range(4,n+1):
    x=[]
    for k in range((i-2)//2):
        x.append(a[k]^a[i-4-k])
    x.append(a[i-3])
    for y in range(max(x)+2):
        if x.count(y)==0:
            t=y
            break
    a.append(t)
if a[n-1]:
    print(1)
else:
    print(2)
