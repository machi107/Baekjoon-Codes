while(1):
    try:
        x=list(map(int,input().split()))
        a=x[0]
        q="J"
        t=[]
        for i in range(1,a):z=x[i]-x[i+1];t.append(max(z,-z))
        t.sort()
        for i in range(a-1):
            if t[i]!=i+1:q="Not j";break
        print(q+"olly")
    except:
        break
