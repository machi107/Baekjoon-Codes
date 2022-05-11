import sys
z=sys.stdin.readline
x=[]
for i in range(int(z())):x.append(int(z()))
x.sort()
print(*x,sep="\n")
