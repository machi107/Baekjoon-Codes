while(1):
    a=input()
    if a=="#":break
    x=[]
    q=""
    while(a!='*'):
        q+=a
        a=input()
    t=1
    o=0
    for i in range(len(q)):
        if q[i]==" ":
            t+=1
            t%=2
            o=1
        else:
            if o==1:x.append(t)
            o=0
            t=1
    if len(x)==0:x.append(0)
    for _ in range(5):
        if len(x)%5:
            x.append(0)

    ans=[]
    qq=""
    for i in range(len(x)):
        qq+=str(x[i])
        if len(qq)==5:
            ans.append(int(qq,2))
            qq=""
    for i in range(len(ans)):
        ans[i]=ans[i]+64
        if ans[i]==64:ans[i]=" "
        elif ans[i]<=ord("Z"):ans[i]=chr(ans[i])
        elif ans[i]==91:ans[i]="'"
        elif ans[i]==92:ans[i]=","
        elif ans[i]==93:ans[i]="-"
        elif ans[i]==94:ans[i]="."
        elif ans[i]==95:ans[i]="?"
        else:ans[i]=""
    an=""

    for i in ans:
        an+=i
    print(an)
