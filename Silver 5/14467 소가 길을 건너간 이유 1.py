x=[2 for _ in range(10)]
r=0
for i in range(int(input())):
    a,b=map(int,input().split())
    if x[a-1]==2:r-=1
    if x[a-1]!=b:r+=1
    x[a-1]=b
print(r)
