import sys
import math

in_put = sys.stdin.readline


a= int(in_put())
n=2
while (a>n):
    if a%n ==0:
        print(n)
        a=a//n
        n=2
    else:
        n+=1

if(a!=1):
    print(a)
