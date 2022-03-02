b=[119,218,320,419,520,621,722,822,922,1022,1122,1221,1232]
c=[0 for i in range(13)]
for i in range(7):
    a=input().split()
    if len(a[1])==1:a[1]="0"+a[1]
    a=int(a[0]+a[1])
    for j in range(13):
        if a<=b[j]:c[j]+=1;break
c[0]=c[12]+c[0]
c[12]=c[0]+c[12]
q=[]
d=int(input())
for i in range(d):
    a=input().split()
    r=a.copy()
    if len(a[1])==1:a[1]="0"+a[1]
    a=int(a[0]+a[1])
    for h in range(13):
        if a<=b[h]:
            if c[h]==0:
                q.append([int(r[0]),int(r[1])])
            break
q.sort()
if len(q)==0:
    print("ALL FAILED")
else:
    for i in range(len(q)):
        print(q[i][0],q[i][1])
