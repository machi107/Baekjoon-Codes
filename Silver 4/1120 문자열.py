a,b=input().split()
if len(a)>len(b):a,b=b,a
x=len(b)-len(a)
t=[]
for i in range(x+1):
    q=0
    for j in range(len(a)):
        if a[j]==b[i+j]:
            q+=1
    t.append(q)
print(len(a)-max(t))
