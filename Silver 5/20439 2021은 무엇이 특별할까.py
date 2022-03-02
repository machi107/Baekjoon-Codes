x,z=[],[]
for i in range(2,110):
    t=1
    for j in range(2,i):
        if i%j==0:t=0;break
    if t:x.append(i)
for i in range(len(x)-1):
    z.append(x[i]*x[i+1])
r=int(input())
for i in z:
    if r<i:print(i);break
