import sys





in_put = sys.stdin.readline

n= int(in_put())
c=[]
d=[]
for i in range(n):
    a,b = map(int,in_put().split())
    c.append([a,b])


for i in range(n):
    count=1
    for j in range(n):
        if c[i][0]<c[j][0] and c[i][1]<c[j][1]:
            count +=1
    d.append(count)

for i in range(len(d)):
    print(d[i],end=" ")
