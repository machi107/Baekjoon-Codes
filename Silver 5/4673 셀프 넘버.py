import sys

in_put = sys.stdin.readline


def selfnum(n):
    a=b=c=d=0
    if n >= 1000:
        a = n // 1000
    if n >= 100:
        b = (n//100 )%10
    if n >= 10:
        c = (n//10)%10
    d= n%10

    return n+a+b+c+d



d=[]
for i in range(1,10000):
    d.append(selfnum(i))



for i in range(1,10000):
    if not d.count(i):
        print(i)
