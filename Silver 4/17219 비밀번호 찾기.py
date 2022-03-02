import sys
import itertools
in_put = sys.stdin.readline

a,b=map(int,in_put().split())

x={}
for i in range(a):
    c,d=in_put().rstrip("\n").split()
    x.setdefault(c,d)

for j in range(b):
    print(x.get(in_put().rstrip("\n")))
