import sys
x=sys.stdin.readline
a=int(input())
for i in range(a):
    b,c,d=map(int,x().split())
    if b==1:
        if c%2 and d%2:r=1
        else:r=0
    elif min(c,d)<=b:
        if (d+c)%2:r=0
        else:r=1
    elif min(c,d)%(b+1)==0:r=0
    else:
        t=(min(c,d)//(b+1)%2)
        if (c+d)%2:r=1
        else:r=0
        if t==0:r-=1
    print("cubelover") if r else print("koosaga")
