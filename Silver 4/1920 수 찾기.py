import sys


in_put = sys.stdin.readline

a= int(in_put())

x=list(map(int,in_put().split()))
x.sort()

b= int (in_put())

xx=list(map(int,in_put().split()))

for i in range(b):
    t=a
    z=0
    while(1):
        if xx[i]== x[(t+z)//2]:
            print(1)
            break
        elif xx[i] < x[(t+z)//2]:
            t=(t+z)//2
        elif xx[i] > x[(t+z)//2]:
            z=(t+z)//2

        if t-1<=z:
            if xx[i] ==  x[(t+z)//2]:
                print(1)
            else:
                print(0)
            break
