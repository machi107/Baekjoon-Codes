a=int(input())
x=list(map(int,input().split()))
t=x[0]
for i in range(1,a):t=(t^x[i])
z=0
for i in x:
    if i^t<i:z+=1
print(z)
