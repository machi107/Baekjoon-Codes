a,c=input().split("=")
a,b=a.split("+")
x=""
z=[0,0,0]
q=[0,0,0]
r=[0,0,0]
for i in range(len(a)):
    if a[i].isdigit():
        x+=x[-1]*(int(a[i])-1)
    else:
        x+=a[i]
o=""
for i in range(len(b)):
    if b[i].isdigit():
        o+=o[-1]*(int(b[i])-1)
    else:
        o+=b[i]
w=""
for i in range(len(c)):
    if c[i].isdigit():
        w+=w[-1]*(int(c[i])-1)
    else:
        w+=c[i]
wor="CHO"
for i in range(len(x)):
    n=wor.find(x[i])
    z[n]+=1
for i in range(len(o)):
    n=wor.find(o[i])
    q[n]+=1
for i in range(len(w)):
    n=wor.find(w[i])
    r[n]+=1
wt=0
for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if z[0]*i+q[0]*j==r[0]*k:
                if z[1]*i+q[1]*j==r[1]*k:
                    if z[2]*i+q[2]*j==r[2]*k:
                        wt=1
            if wt:
                break
        if wt:
            break
    if wt:
        break
print(i,j,k)
            
            
