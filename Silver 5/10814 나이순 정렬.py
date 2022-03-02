import sys
in_put = sys.stdin.readline


a=int(in_put())
c= [[0,0,0]]*a

for i in range(a):
    b,d =in_put().split()
    b= int(b)
    d= d.rstrip("\n")
    c[i]=b,i,d

c.sort()




for j in range(a):
    print(c[j][0], c[j][2])
