n=int(input())
a=input()
b=input()
k="YES"
x=""
y=""
t=[]
p=[]
if a[0]!=b[0] or a[-1]!=b[-1]:k="NO"
for i in range(1,n-1):
    if a[i] not in ['a','e','i','o','u']:x+=a[i]
    t.append(a[i])
    if b[i] not in ['a','e','i','o','u']:y+=b[i]
    p.append(b[i])
if x!=y:k="NO"
p.sort()
t.sort()
if t!=p:k="NO"
print(k)
