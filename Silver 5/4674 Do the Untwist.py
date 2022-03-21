a=input()
while(a!="0"):
    b,c=a.split()
    b=int(b)
    n=len(c)
    x=[]
    z=[]
    r=""
    for i in range(n):
        if c[i]==".":x.append(27)
        elif c[i]=="_":x.append(0)
        else:x.append(ord(c[i])-96)
        z.append(0)
    for i in range(n):z[b*i%n]=(x[i]+i)%28
    for i in range(n):
        if z[i]==0:r+="_"
        elif z[i]==27:r+="."
        else:r+=chr(z[i]+96)
    print(r)
    a=input()
