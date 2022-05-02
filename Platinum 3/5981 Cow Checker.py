import math
r=input()
for i in range(int(input())):
    x,y=map(int,input().split())
    x,y=max(x,y),min(x,y)
    y=x-y
    q=y+int(y*((1+(math.sqrt(5)))/2))
    print("Bessie") if q!=x else print("Farmer John")
