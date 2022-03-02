while(1):
    x,a=[],int(input())
    if a==0:break
    for i in range(a):t=input();x.append(t.lower()+" "+t)
    x.sort()
    print(x[0][len(x[0])//2+1:])
