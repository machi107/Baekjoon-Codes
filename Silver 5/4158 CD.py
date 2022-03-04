import sys
q=sys.stdin.readline

a,b=map(int,input().split())
while(a+b):
    x,y=[],[]
    for i in range(a):x.append(int(q()))
    for j in range(b):y.append(int(q()))
    print(len(set(x)&set(y)))
    a,b=map(int,input().split())
