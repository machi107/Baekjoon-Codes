import sys


in_put = sys.stdin.readline

c,d = map(int,in_put().split(" "))
a,b=max(c,d),min(c,d)

while (1):
    if a%b==0:
        break
    a=a-b
    a,b=max(a,b),min(a,b)
print(b)
print(c*d//b)

