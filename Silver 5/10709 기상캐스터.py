a,b=map(int,input().split())
for i in range(a):
    x,t,q=input(),0,""
    for j in range(b):
        if x[j]=='c':t=1;q+="0"
        elif t:q+=str(t);t+=1
        else:q+="-1"
        q+=" "
    print(q[:-1])
