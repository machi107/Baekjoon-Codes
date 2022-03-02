import sys

in_put = sys.stdin.readline

a,b=map(int,in_put().split(" "))
x=[]
for _ in range(a):
    x.append(int(in_put()))
x.sort(reverse=True)
coin=0

for i in range(a):
    if x[i]<=b:
        coin+=b//x[i]
        b=b%x[i]


print(coin)
