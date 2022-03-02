for _ in range(int(input())):
    a,b=map(int,input().split())
    t=0
    if a:
        t+=1
    for i in range(b,a,-1):
        t*=i/(i-a)
    print(round(t))
