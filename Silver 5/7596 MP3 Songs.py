a=int(input())
t=1
while(a):
    x=[]
    for i in range(a):x.append(input())
    x.sort()
    print(t)
    for i in x:print(i)
    t+=1
    a=int(input())
