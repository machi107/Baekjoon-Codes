import sys
in_put = sys.stdin.readline

a= int(in_put())

for _ in range(a):
    x,y= map (int,in_put().split())

    prt = list(map(int,in_put().split()))
    count=1
    num=prt[y]
    prt[y]="Target"
   

    for i in range(9,num,-1):
        swit=0
        for h in range(x):
            if prt[h]==i:
                count+=1
                swit=h

        prt=prt[swit:]+prt[:swit]

    for i in range(x):
        if prt[i]=="Target":
            break
        elif prt[i]==num:
            count+=1
    print(count)
