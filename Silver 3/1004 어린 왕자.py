a=int(input())
for _ in range(a):
    x,y,xx,yy=map(int,input().split())
    c=int(input())
    ans=0
    for _ in range(c):
        count=0
        cenx,ceny,leng=map(int,input().split())
        if (x-cenx)**2+(y-ceny)**2<leng**2:
            count+=1
        if (xx-cenx)**2+(yy-ceny)**2<leng**2:
            count+=1
        if count%2:
            ans+=1
    print(ans)
