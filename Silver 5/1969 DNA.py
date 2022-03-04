a,b=map(int,input().split())
t=[[0 for _ in range(26)] for i in range(b)]
for i in range(a):
    k=input()
    for j in range(b):
        t[j][ord(k[j])-64]+=1
q=0
z=""
for i in range(b):
    r=max(t[i])
    q+=sum(t[i])-r
    z+=chr(t[i].index(r)+64)
print(z)
print(q)
