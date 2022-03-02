a=int(input())
z=0
x=list(map(int,input().split()))
y=list(map(int,input().split()))
t=[0 for i in range(1000005)]
for i in range(a):t[x[i]]+=1;t[y[i]]-=1
for i in range(len(t)):
    if t[i]>0:z+=t[i]
print(z)
