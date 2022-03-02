import sys

in_put = sys.stdin.readline

coun = int(in_put())
b=map(int,in_put().split())
c=map(int,in_put().split())
b=list(b)
b.sort()
c=list(c)
c.sort(reverse=True)
x=0
for i in range(coun):
    x+=b[i]*c[i]

print(x)
