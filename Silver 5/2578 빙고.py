x,z,q=[],[],[]
for i in range(5):x.append(list(map(int,input().split())))
for i in range(5):x.append([x[0][i],x[1][i],x[2][i],x[3][i],x[4][i]]);z.append(x[i][i]);q.append(x[4-i][i])
x.append(z)
x.append(q)
t=""
for j in range(5):t+=input()+" "
t=list(map(int,t.split()))
for i in range(25):
    r=0
    for j in range(12):
        if len(x[j])==0:r+=1
        if t[i] in x[j]:x[j].remove(t[i])
    if r>2:break
print(i)
