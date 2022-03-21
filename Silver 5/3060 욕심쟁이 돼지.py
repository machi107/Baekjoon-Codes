a=int(input())
for i in range(a):
    x,r=int(input()),1
    t=sum(list(map(int,input().split())))
    while(t<=x):t*=4;r+=1
    print(r)
