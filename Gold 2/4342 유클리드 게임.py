a,b=map(int,input().split())
q=["A","B"]
while(a+b):
    t=0
    a,b=max(a,b),min(a,b)
    while(1):
        if a%b==0:break
        elif a>b*2:break
        else:a,b=b,a-b;t+=1
    print(q[t%2]+" wins")
    a,b=map(int,input().split())
