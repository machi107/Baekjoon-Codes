import sys
t=sys.stdin.readline

k=[]
for i in range(int(t())):
    a,b=t().split()
    if b[0]=="e":k.append(a)
    else:k.remove(a)
k.sort(reverse=True)
print(*k,sep="\n")
