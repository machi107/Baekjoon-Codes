for i in range(int(input())):
    a,b=map(int,input().split())
    t=0
    for j in range(a,b+1):t+=str(j).count("0")
    print(t)
