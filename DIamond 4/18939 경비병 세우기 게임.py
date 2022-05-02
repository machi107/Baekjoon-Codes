import sys
L=sys.stdin.readline
a=int(input())
for i in range(a):
    r=0
    b,c,d=map(int,L().split())
    r+=b*c%2
    if max(b,c)<d*2:r=1
    print("Yuto")if r else print("Platina")
