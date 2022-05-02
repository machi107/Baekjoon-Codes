while(1):
    try:
        a,b=map(int,input().split())
        q=0
        for i in range(a,b+1):
            if len(str(i))==len(set(str(i))):q+=1
        print(q)
    except:
        break
