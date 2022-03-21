x="A BC D EF G "
r=[1,1,1,1,1,1,1]
q=[0,2,3,5,7,8,10]
a=int(input())
for i in range(a):
    t=int(input())
    for j in range(7):
        q[j]=q[j]+t
        while(q[j]>11):q[j]-=12
        while(q[j]<0):q[j]+=12
        if x[q[j]]==" ":r[j]=0
for i in range(7):
    if r[i]:
        print(chr(i+65),x[q[i]])
