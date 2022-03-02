import sys

in_put = sys.stdin.readline
d=[]
ans=[]
repairL=[]
repairP=[]
for _ in range(4):
    a=in_put().rstrip("\n")
    d.append(a)
while (1):
    a=in_put().rstrip("\n")
    if a!="":
        break
ans.append(a)
for _ in range(3):
    a=in_put().rstrip("\n")
    ans.append(a)

for i in range(4):
    for j in range(4):
        if d[i][j]!=ans[i][j] and d[i][j]=='L':
            repairL.append([i,j])
        elif d[i][j]!=ans[i][j] and d[i][j]=='P':
            repairP.append([i,j])
xxx=0



while(len(repairL)):
    c=500
    for i in range(len(repairP)):
        a=repairL[0][0]-repairP[i][0]
        b=repairL[0][1]-repairP[i][1]
        if a<0:
            a= -a
        if b<0:
            b= -b
        
        if a+b<c:
            d=i
            c=a+b
    xxx+=c
    repairL.pop(0)
    repairP.pop(d)

print(xxx)
        
