import sys

in_put = sys.stdin.readline


a=int(in_put())
c= [[0,0]]*a

for i in range(a):
    d = in_put().rstrip("\n")
    c[i]=len(d),d

c.sort()




for j in range(a):
    if j == 0:
        print(c[j][1])
    if j>0 and c[j][1] != c[j-1][1]:
        print(c[j][1])


