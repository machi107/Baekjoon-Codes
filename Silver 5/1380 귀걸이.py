z=1
while(1):
    a=int(input())
    x=[]
    t=0
    if a==0:
        break
    for i in range(a):
        t+=i*2
        x.append(input())
    for _ in range(a*2-1):
        t-=int(input().split()[0])-1
    print(z,x[t])
    z+=1
