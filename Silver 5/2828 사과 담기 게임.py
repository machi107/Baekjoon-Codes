a,b=map(int,input().split())
p=b
z=0
c=int(input())
for i in range(c):
    d=int(input())
    if d>p:z+=d-p;p=d
    elif p-b+1>d:z+=p-b+1-d;p=d+b-1
print(z)
