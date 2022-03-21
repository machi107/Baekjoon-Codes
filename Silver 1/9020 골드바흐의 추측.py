import sys

in_put = sys.stdin.readline

def HA(n):
    for q in range(2,n):
        if n//q == n/q:
            return 0
    return True
        

a=int(in_put())

for i in range(a):
    b= int(in_put())
    c=b//2
    count=1
    for j in range(c):
        if HA(c+j) and HA(c-j):
            print (c-j,c+j,sep=" ")
            break
        
