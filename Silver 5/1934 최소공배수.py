import sys
in_put = sys.stdin.readline

a=int(in_put())

for _ in range(a):
    b,c=map(int,in_put().split())
    t,q=b,c

    while(1):
        if max(b,c)%min(b,c)==0:
            break
        else:
            b,c=max(b,c)-min(b,c),min(b,c)

    

    print(t*q//min(b,c))
            
