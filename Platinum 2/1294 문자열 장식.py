a=int(input())
x=[]
for i in range(a):x.append(list(input()))
y=""
while(1):
    q=[]
    for i in range(a):
        if len(x[i]):q.append(x[i])
    if len(q)==0:break
    q.sort()
    z=q[0]
    for i in range(len(q)):
        if z==q[i][:len(z)]:z=q[i]
        else:break
    y+=z[0]
    for i in range(a):
        if len(x[i]) and x[i]==z:del x[i][0];break
print(y)
