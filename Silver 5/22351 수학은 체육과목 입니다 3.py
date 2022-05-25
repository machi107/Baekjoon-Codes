a=input()
while(1):
    x=a[0]
    r=int(x)+1
    while(x!=a and r<1000):
        x+=str(r)
        r+=1
    if x==a:print(a[0]+" "+str(r-1));break
    y=a[0]+a[1]
    r=int(y)+1
    while(y!=a and r<1000):
        y+=str(r)
        r+=1
    if y==a:print(a[0]+a[1]+" "+str(r-1));break
    z=a[0]+a[1]+a[2]
    r=int(z)+1
    while(z!=a and r<1000):
        z+=str(r)
        r+=1
    if z==a:print(a[0]+a[1]+a[2]+" "+str(r-1));break
