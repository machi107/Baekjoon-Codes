import sys
in_put = sys.stdin.readline

zz,mok= map(int,in_put().split())

x=list(map(int,in_put().split()))

x.sort(reverse=True)


a=x[0]

b=x[0]-mok


while(1):
    t=(a+b)//2
    tree=0
    for i in range(zz):
        tree+=max(x[i]-t,0)
    if tree == mok:
        break

    if tree>mok:
        if a-1<=b:
            break
        b=t
    elif tree<mok:
        if a-1<=b:
            break
        a=t

print(t)

## pypy3 에서만 통과한 코드
