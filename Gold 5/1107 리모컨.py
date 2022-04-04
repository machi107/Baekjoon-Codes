a=int(input())
b=int(input())
if b:
    c=set(input().split())
else:
    c=set("")
z=max(100-a,a-100)
if len(c)==10:
    print(z)
else:
    x=1000002
    t=0
    for i in range(a,-1,-1):
        if len(c&set(str(i)))==0:
            t=1
            break
    if t:x=i
    t=0
    y=1000002
    for i in range(a,1000001):
        if len(c&set(str(i)))==0:
            t=1
            break
    if t:y=i
    u=len(str(x))+max(x-a,a-x)
    o=len(str(y))+max(y-a,a-y)
    print(min(z,o,u))
   
