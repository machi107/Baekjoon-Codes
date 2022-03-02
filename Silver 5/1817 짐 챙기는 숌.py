a,b=map(int,input().split())
x,t,r=[],0,0
if a:x=list(map(int,input().split()));r+=1
for i in range(a):
    if t+x[a-1-i]>b:t=0;r+=1
    t+=x[a-1-i]
print(r)
