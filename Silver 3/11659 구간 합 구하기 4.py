import sys
t=sys.stdin.readline
a,b=map(int,t().split())
x=list(map(int,t().split()))
for i in range(1,a):x[i]+=x[i-1];
x.insert(0,0)
for i in range(b):c,d=map(int,t().split());print(x[d]-x[c-1])
