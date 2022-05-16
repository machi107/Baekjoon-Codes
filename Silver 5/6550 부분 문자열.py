while True:
    try:
        a,b=input().split()
        q=len(b)
        s=len(a)
        z=0
        p=0
        while(z!=q and s!=p):
            if a[p]==b[z]:p+=1
            z+=1
        print("Yes"if s==p else "No")
    except:break
