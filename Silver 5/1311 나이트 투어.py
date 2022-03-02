x=[[0 for _ in range(6)] for _ in range(6)]
a="ABCDEF"
s=0
for r in range(36):
    t=input()
    if r:
        w=ord(s[0])-ord(t[0])
        v=ord(s[1])-ord(t[1])
        w=max(w,-w)
        v=max(v,-v)
        if (w!=1 or v!=2) and (v!=1 and w!=2):
            x[0][0]=7
            break
    else:
        p=t
    if r==35:
        w=ord(p[0])-ord(t[0])
        v=ord(p[1])-ord(t[1])
        w=max(w,-w)
        v=max(v,-v)
        if (w!=1 or v!=2) and (v!=1 and w!=2):
            x[0][0]=7
            break
    
    s=t
    x[a.find(t[0])][int(t[1])-1]=1
q="Valid"

for i in range(6):
    if sum(x[i])!=6:
        q="Inv"+q[1:]
        break
print(q)
