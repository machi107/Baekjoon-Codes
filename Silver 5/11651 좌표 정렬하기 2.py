import sys

in_put = sys.stdin.readline


a=int(in_put())

b=[[0,0]]*a

for i in range(a):
    c,d=map(int,in_put().split())
    b[i]=d,c

b.sort()

for j in range(a):
    print (b[j][1], b[j][0])

