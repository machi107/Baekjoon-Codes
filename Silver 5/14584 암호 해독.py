a=input()
x=[]
r=[]
for i in range(int(input())):x.append(input())
r.append(a)
for i in range(1,26):
    q=""
    for h in range(len(a)):
        t=ord(a[h])+i
        if t>122:t-=26
        q+=chr(t)
    r.append(q)
for i in range(26):
    for j in range(len(x)):
        if x[j] in r[i]:ans=r[i]
print(ans)
