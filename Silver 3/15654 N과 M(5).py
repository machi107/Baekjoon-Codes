import itertools
a,b=map(int,input().split())
t=1
x=list(map(int,input().split()))
x.sort()
q=list(itertools.permutations(x,b))
for i in range(len(q)):print(" ".join(map(str,q[i])))
