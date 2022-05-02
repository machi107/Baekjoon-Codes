a,b=map(int,input().split())
c=list(map(int,input().split()))
q=[0,2,5]
r=[1,3]
f=0
if b%2:
    for i in range(a):
        t=0
        if c[i]<7:
            if c[i]in q:t=0
            elif c[i]in r:t=1
            else:t=2
        elif c[i]%2:t=0
        else:
            while(c[i]%2==0 and c[i]>7):t+=1;c[i]=c[i]//2
            t=t%2+1
        f^=t
else:
    for i in range(a):
        if c[i]==2:f^=2
        else:f^=(c[i]-1)%2
print("Kevin") if f else print("Nicky")
