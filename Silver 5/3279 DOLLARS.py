a=int(input())
q=[]
for i in range(a):
    q.append(int(input()))
t=0
j=0
r=[]
while(1):
    for i in range(j,a):
        if t>q[i]:
            r.append(q[i-1])
            i-=1
            break
        t=q[i]
    if i==a-1:
        if len(r)%2:
            r=r[:-1]
        break
    for j in range(i,a):
        if t<q[j]:
            r.append(q[j-1])
            j-=1
            break
        t=q[j]
    if j==a-1:
        if len(r)%2:
            r.append(q[j])
        break
ans=100
for i in range(len(r)):
    if i%2:
        ans/=r[i]
    else:
        ans*=r[i]
print("{:.2f}".format(ans))
