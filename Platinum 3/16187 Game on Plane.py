import sys
x=sys.stdin.readline
a=int(input())
z=[0,4,8,14,20,24,28,34,38,42,54,58,62,72,76,88,92,96,102]
for i in range(a):
    q=int(x())-1
    if q>77:q=q%34+68
    print("Second") if q in z else print("First")
