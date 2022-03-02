input()
x=list(map(int,input().split()))
x.append(0)
x.sort()
t=int(input())
for i in range(len(x)):
    if x[i]>t:break
r=(t-x[i-1])*(x[i]-t)
if r:r-=1
print(r)
