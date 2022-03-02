import sys
in_put=sys.stdin.readline

a= int(in_put())
x=[]
for _ in range(a):
    t=int(in_put())
    if t:
        x.append(t)
    else:
        x.pop()
print(sum(x))
