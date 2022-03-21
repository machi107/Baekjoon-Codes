a=int(input())
for i in range(a):
    t=[]
    y=[]
    b,c,d,e=map(int,input().split())
    for i in range(max(b,c)):
        t.append(d+b*i)
        y.append(e+c*i)
    z=list(set(t)&set(y))
    z.sort()
    if len(z):
        print(z[0])
    else:
        print(-1)
