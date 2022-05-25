a=[]
c=int(input())
for _ in range(c):
    b=list(input().split())
    a.append(b[1:])
a.sort()
x=[0 for i in range(15)]
for i in range(c):
    for j in range(len(a[i])):
        if x[j]!=a[i][j]:
            print("--"*j+a[i][j])
            x[j]=a[i][j]
            for k in range(j+1,len(a[i])):
                x[k]=0
