import sys

in_put = sys.stdin.readline


a=int(in_put())

b=[[0,0]]*a

for i in range(a):
    c,d=map(int,in_put().split())
    b[i]=c,d

b.sort()

for j in range(a):
    print (b[j][0], b[j][1])
