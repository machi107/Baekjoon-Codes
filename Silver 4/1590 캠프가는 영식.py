a,b=map(int,input().split())
x=[]
for i in range(a):
    d,e,f=map(int,input().split())
    for h in range(f):
        if d>=b:
            x.append(d)
            break
        d+=e
print(min(x)-b) if len(x) else print(-1)
