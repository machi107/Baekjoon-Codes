for i in range(int(input())):
    a,b=map(int,input().split())
    t=[]
    for h in range(b):x,y=map(int,input().split());t.append(x*y)
    t.sort()
    p=0
    while(a>0):p+=1;a-=t[-1];t.pop()
    print(p)
