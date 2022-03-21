a,b=map(int,input().split())
c=int(input())
d=[]
for i in range(c):d.append(int(input()))
t=150000
for i in range(c):
    q=max(b-d[i],d[i]-b)
    if t>q:t=q
if t+1<=max(a-b,b-a):print(t+1)
else: print(max(a-b,b-a))
