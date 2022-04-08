import sys
s=sys.stdin.readline
a=int(input())
for i in range(a):
    r=int(s())
    r=(r-1)*2
    q=4
    while(q<r):
        q*=4
    while(r and q):
        if r>=q:r-=q
        q=q//4
    if r:print("cubelover")
    else:print("koosaga")
