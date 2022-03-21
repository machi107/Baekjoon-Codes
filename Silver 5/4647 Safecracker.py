a,b=input().split()
v=[]
w=[]
x=[]
y=[]
z=[]
for i in range(26):
    q=i+1
    v.append(q)
    w.append(q**2)
    x.append(q**3)
    y.append(q**4)
    z.append(q**5)
while(a!='0' and b!='end'):
    a=int(a)
    t=[]
    ans="no solution"
    for i in range(len(b)):
        t.append(ord(b[i])-65)
    t.sort()
    for i in range(len(t)):
        for ii in range(len(t)):
            for iii in range(len(t)):
                for iiii in range(len(t)):
                    for iiiii in range(len(t)):
                        if v[t[i]]-w[t[ii]]+x[t[iii]]-y[t[iiii]]+z[t[iiiii]]==a and len(set([i,ii,iii,iiii,iiiii]))==5:
                            ans=chr(t[i]+65)+chr(t[ii]+65)+chr(t[iii]+65)+chr(t[iiii]+65)+chr(t[iiiii]+65)
    print(ans)
    
    a,b=input().split()
