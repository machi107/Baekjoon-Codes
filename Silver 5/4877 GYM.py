a=list(map(int,input().split()))
t=[]
z=len(a)
sa=sum(a)
for i in range(z):
    a[i]=a[i]/sa
t.append(a)
for i in range(z-1):
    b=list(map(int,input().split()))
    sa=sum(b)
    for j in range(z):
        b[j]=b[j]/sa
    t.append(b)

x=[[0 for _ in range(z)] for _ in range(10)]
x[0][0]=1
for i in range(1,10):
    for j in range(z):
        for q in range(z):
            x[i][j]+=x[i-1][q]*t[q][j]

for i in range(10):
    for j in range(z):
        if j!=z-1:
            print("{:.5f}".format(x[i][j]),end=" ")
        else:
            print("{:.5f}".format(x[i][j]))
