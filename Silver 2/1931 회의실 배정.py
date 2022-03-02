import sys
in_put = sys.stdin.readline

a=int(in_put())
x=[]
for _ in range(a):
    st,en = map(int,in_put().split())
    x.append([en,st])
x.sort()


ans=0
if len(x):
    t=x[0][0]
    ans+=1

for i in range(1,a):
    if x[i][1]>=t:
        t=x[i][0]
        ans+=1
print(ans)
