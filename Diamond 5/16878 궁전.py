import sys
t=sys.stdin.readline
a=[1,1,0,0,2]
x=int(input())
q=4
for j in range(x):
    r=int(t())
    if r>q:
        for i in range(q+1,r+1):
            a.append(((i+1)*a[i-1]-(i-2)*a[i-2]-(i-5)*a[i-3]+(i-3)*a[i-4])%1000000007)
        q=r
        print(a[r])
    else:
        print(a[r])
