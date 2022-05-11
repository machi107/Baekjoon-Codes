for i in range(int(input())):
    x,z=[],0
    for j in range(int(input())):x.append(input())
    for t in range(len(x)):
        for q in range(len(x)):
            p=x[t]+x[q]
            if t!=q and p==p[::-1]:z=1;break
        if z:break
    print(p if z else 0)
