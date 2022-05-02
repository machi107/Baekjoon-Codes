a=int(input())
q=[1]
p=1
while(p!=a):p*=3;q.append(p)
k=len(q)
for i in range(a):
    for j in range(a):
        z=1
        for t in range(k): 
            if i//q[t]%3==1 and j//q[t]%3==1:print(" ",end="");z=0;break
        if z:print("*",end="")
    print("")
