a=int(input())
for _ in range(a):
    x=list(map(int,input().split()))
    x.sort()
    print(x[7])
