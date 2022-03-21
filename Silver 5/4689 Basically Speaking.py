x=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while True:
    try:
        a,b,c=input().split()
        r=(int(a,int(b)))
        ans=""
        c=int(c)
        while(r):
            ans+=x[r%c]
            r=r//c
        if len(ans)>7:ans="RORRE  "
        else:ans+=" "*(7-len(ans))
        print(ans[::-1])
    except:break
