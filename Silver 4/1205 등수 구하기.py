a,b,c= map(int,input().split())
d=[]
if a:
    d=list(map(int,input().split()))
while(len(d)!=c):
    d.append(-1)
for i in range(len(d)):
    if d[i]<=b:
        break
if b<=d[-1]:
    i=-2
print(i+1)
