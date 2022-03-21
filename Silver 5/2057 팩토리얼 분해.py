x=[1]
t=1
k=1
while(k<1000000000000000000):
    x.append(k)
    t+=1
    k*=t
t=int(input())
a=0
x.sort(reverse=True)
for i in range(len(x)):
    if t>=a+x[i]:a+=x[i]
if a==t and a:print("YES")
else:print("NO")
