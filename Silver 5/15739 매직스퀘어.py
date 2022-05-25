x=[]
l=int(input())
for i in range(l):x.append(list(map(int,input().split())))
k=[]
for i in x:k.append(sum(i))
p=0
q=0
r=[]
for j in range(l):p+=x[l-j-1][j];q+=x[j][l-j-1]
for i in range(l):
    z=0
    for j in range(l):
        z+=x[j][i]
        r.append(x[j][i])
    k.append(z)
k.append(p)
k.append(q)
print("TRUE" if len(set(k))==1 and len(set(r))==l*l else "FALSE")
