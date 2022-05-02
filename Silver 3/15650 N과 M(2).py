import itertools
a,b=map(int,input().split())
t=1
x=[i+1 for i in range(a)]
q=list(itertools.combinations(x,b))
for i in range(len(q)):print(" ".join(map(str,q[i])))
