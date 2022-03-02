from itertools import combinations
a=int(input())
x=0
t=0
for i in range(a):
    b=list(map(int,input().split()))
    res=list(combinations(b,3))
    for j in range(len(res)):res[j]=sum(res[j])%10
    if x<=max(res):x=max(res);t=i+1
print(t)
