import sys
import math

in_put = sys.stdin.readline

n = int(in_put())

for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    if x1 != x2 or y1 != y2:
        
        Swi = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) - (r2+r1)*(r2+r1)
        if Swi == 0:
            print (1)
        elif Swi > 0:
            print (0)
        else:
            Swi2 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) - (r2-r1)*(r2-r1)
            if Swi2 == 0:
                print(1)
            elif Swi2 > 0:
                print (2)
            else:
                print (0)


    else:
        if r1 == r2:
            print(-1)
        else :
            print(0)
