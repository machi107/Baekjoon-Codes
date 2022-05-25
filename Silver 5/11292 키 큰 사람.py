while(1):
    a=int(input())
    if a==0:break
    x=[]
    t=[]
    for i in range(a):
        b,c=input().split()
        x.append(float(c))
        t.append([float(c),b])
    p=max(x)
    z=""
    for i in range(a):
        if p==t[i][0]:
            z+=" "+t[i][1]
    print(z[1:])
