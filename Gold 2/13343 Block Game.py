a,b=map(int,input().split())
q=["win","lose"]
t=0
a,b=max(a,b),min(a,b)
while(1):
    if a%b==0 or a>b*2:break
    else:a,b=b,a-b;t+=1
print(q[t%2])
