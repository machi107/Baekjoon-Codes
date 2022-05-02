a=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
t=[]
for i in range(a):
    q=[]
    for j in range(a):q.append(max(x[i]-y[j],y[j]-x[i]))
    t.append(min(q))
print(max(t))
