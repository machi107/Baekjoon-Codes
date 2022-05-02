a,b=map(int,input().split())
q=0
for i in range(a):
    r=(list(map(int,input().split())))
    while(len(r) and r[0]==0):
        del r[0]
    while(len(r)>1 and r[1]==0):
        del r[1]
    if len(r)==1:t=r[0]
    elif len(r)==0:t=0
    elif r[0]>r[1]:t=r[0]
    elif r[0]<r[1]:t=r[0]-1
    else:
        r.append(0)
        for j in range(len(r)):
            if r[0]!=r[j] and r[j]!=0:break
        if r[0]>r[j]-j%2:t=r[0]-1
        else:t=r[0]
    q^=t
if q:print("koosaga")
else:print("cubelover")
